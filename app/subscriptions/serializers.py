from rest_framework import serializers


class UpdatePlanSerializer(serializers.Serializer):
    plan_id = serializers.CharField(
        max_length=255, help_text="ID do novo plano no Stripe")
