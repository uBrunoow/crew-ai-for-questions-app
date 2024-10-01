from django.core.management.base import BaseCommand
from subscriptions.models import Plans


class Command(BaseCommand):
    help = 'Add predefined plans to the database'

    def handle(self, *args, **kwargs):
        plans = [
            {"name": "FREE", "monthly_price": 0,
                "description": "Plano gratuito", "is_active": True},
            {"name": "PRO", "monthly_price": 19.90,
             "description": "Plano profissional", "is_active": True},
        ]

        for plan in plans:
            Plans.objects.get_or_create(
                name=plan["name"])
            self.stdout.write(self.style.SUCCESS(
                f'Plan {plan["name"]} added or already exists.'))
