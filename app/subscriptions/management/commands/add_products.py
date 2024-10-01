from django.core.management.base import BaseCommand
from subscriptions.models import Products


class Command(BaseCommand):
    help = 'Add predefined products to the database'

    def handle(self, *args, **kwargs):
        products = [
            {"name": "100 Vidas", "price": 100.00,
                "description": "100 VIDAS", "is_active": True},
            {"name": "100 Moedas", "price": 100.00,
             "description": "100 MOEDAS", "is_active": True},
        ]

        for product in products:
            Products.objects.get_or_create(
                name=product["name"])
            self.stdout.write(self.style.SUCCESS(
                f'Product {product["name"]} added or already exists.'))
