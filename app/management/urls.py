from management import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet)
router.register(r'update-stripe-info',
                views.UserUpdateStripeInfoViewSet, basename='update-stripe-info')
router.register(r"register-user", views.UserRegister, basename="register-user")
urlpatterns = [
    path('update-stripe-info/<str:email>/', views.UserUpdateStripeInfoViewSet.as_view(
        {'patch': 'partial_update'}), name='update-stripe-info'),
    path('update-stripe-info/find-user/',
         views.UserUpdateStripeInfoViewSet.as_view({'get': 'find_user'}), name='find-user'),
    path('update-stripe-info/update-stripe/<str:id>/',
         views.UserUpdateStripeInfoViewSet.as_view({'patch': 'update_stripe'}), name='update-stripe'),

    path("logout/", views.LogoutView.as_view()),
    path(
        "change_password/<int:pk>/",
        views.UserChangePasswordView.as_view(),
        name="auth_change_password",
    ),
    path("", include(router.urls)),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path('stripe/webhook/', views.StripeWebhookView.as_view(), name='stripe-webhook'),
]
