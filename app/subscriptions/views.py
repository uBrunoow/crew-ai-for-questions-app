from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
import stripe
from management.models import User
from .serializers import UpdatePlanSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY


class UpdatePlanView(APIView):
    def post(self, request, user_id):
        serializer = UpdatePlanSerializer(data=request.data)
        if serializer.is_valid():
            plan_id = serializer.validated_data['plan_id']
            try:
                user = User.objects.get(id=user_id)
                # Obter o cliente do Stripe
                customer = stripe.Customer.retrieve(str(user.id))

                # Obter a assinatura atual do cliente
                subscriptions = stripe.Subscription.list(customer=customer.id)
                if subscriptions.data:
                    subscription = subscriptions.data[0]
                    # Atualizar a assinatura com o novo plano
                    stripe.Subscription.modify(
                        subscription.id,
                        items=[{
                            'id': subscription['items']['data'][0].id,
                            'price': plan_id,
                        }],
                    )
                    return Response({"message": "Plano atualizado com sucesso"}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Nenhuma assinatura encontrada para este usuário"}, status=status.HTTP_404_NOT_FOUND)
            except User.DoesNotExist:
                return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
            except stripe.error.StripeError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
