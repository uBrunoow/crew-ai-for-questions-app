from django.urls import path
from subscriptions import views

urlpatterns = [
    path("update-plan/<int:user_id>/",
         views.UpdatePlanView.as_view(), name="update-plan"),
]
