import stripe
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import BlacklistedToken, OutstandingToken
from rest_framework.response import Response
from rest_framework import (
    generics,
    mixins,
    permissions,
    response,
    status,
    views,
    viewsets,
)
from utils.actions import DRFAction
from .models import User
from .serializers import (
    ProfileTokenObtainPairSerializer,
    UserChangePasswordSerializer,
    UserCompleteReadOnlySerializer,
    UserRegisterSerializer,
    UserReadOnlySerializer,
    UserFlatSerializer,
    UserUpdateStripeInfoSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from itertools import chain
from django.shortcuts import get_object_or_404, Http404
from rest_framework.filters import SearchFilter
import django_filters
from rest_framework.decorators import action
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.permissions import AllowAny
from datetime import datetime
from subscriptions.models import Transaction


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['is_active', 'email']


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserCompleteReadOnlySerializer
    queryset = User.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["name"]
    filterset_class = UserFilter

    def get_serializer_class(self):
        return (
            self.serializer_class
            if DRFAction.is_list(self.action)
            else UserReadOnlySerializer
        )

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all().order_by('id')
        return User.objects.filter(id=self.request.user.id).order_by('id')

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def flat(self, request):
        queryset = self.get_queryset()
        # Aplique o filtro ao queryset
        filter_backend = DjangoFilterBackend()
        queryset = filter_backend.filter_queryset(request, queryset, self)
        serializer = UserFlatSerializer(queryset, many=True)
        return Response(serializer.data)


class UserRegister(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.none()

    def perform_create(self, serializer):
        res = super().perform_create(serializer)
        return res


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BlacklistedToken.objects.none()
    serializer_class = None

    def post(self, request):
        tokens = OutstandingToken.objects.filter(id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return response.Response(status=status.HTTP_205_RESET_CONTENT)


class UserChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all().order_by('id')
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserChangePasswordSerializer


class ProfileTokenObtainPairView(TokenObtainPairView):
    serializer_class = ProfileTokenObtainPairSerializer


class UserUpdateStripeInfoViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['patch'], url_path='update-stripe')
    def update_stripe(self, request, id=None):
        user = get_object_or_404(User, pk=id)
        serializer = UserUpdateStripeInfoSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='find-user')
    def find_user(self, request):
        stripe_subscription_id = request.query_params.get(
            'stripeSubscriptionId')
        stripe_customer_id = request.query_params.get('stripeCustomerId')

        user = User.objects.filter(
            Q(stripeSubscriptionId=stripe_subscription_id) | Q(
                stripeCustomerId=stripe_customer_id)
        ).values('id').first()

        if user:
            return Response(user, status=status.HTTP_200_OK)
        return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, email=None):
        user = get_object_or_404(User, email=email)
        serializer = UserUpdateStripeInfoSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


stripe.api_key = settings.STRIPE_SECRET_KEY


@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
        endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)

        # Handle the event
        if event['type'] == 'customer.subscription.created' or event['type'] == 'customer.subscription.updated':
            self.handle_process_webhook_updated_subscription(
                event['data']['object'])
        elif event['type'] == 'charge.succeeded':
            self.handle_process_webhook_transaction(event['data']['object'])

        # Unhandled event type
        return JsonResponse({'status': 'success'}, status=200)

    def handle_process_webhook_updated_subscription(self, subscription):
        customer_id = subscription['customer']
        stripe_subscription_id = subscription['id']
        stripe_subscription_status = subscription['status']
        stripe_price_id = subscription['items']['data'][0]['price']['id']

        try:
            user = User.objects.get(stripeCustomerId=customer_id)
            user.stripeSubscriptionId = stripe_subscription_id
            user.stripeSubscriptionStatus = stripe_subscription_status
            user.stripePriceId = stripe_price_id
            user.save()
        except User.DoesNotExist:
            pass  # Handle the case where the user does not exist

    def handle_process_webhook_transaction(self, charge):
        customer_id = charge['customer']
        stripe_transaction_id = charge['id']
        amount = charge['amount'] / 100  # Stripe amounts are in cents
        currency = charge['currency']
        status = charge['status']
        created_at = datetime.fromtimestamp(charge['created'])

        try:
            user = User.objects.get(stripeCustomerId=customer_id)
            Transaction.objects.create(
                user=user,
                stripe_transaction_id=stripe_transaction_id,
                amount=amount,
                currency=currency,
                status=status,
                created_at=created_at,
            )
        except User.DoesNotExist:
            pass  # Handle the case where the user does not exist
