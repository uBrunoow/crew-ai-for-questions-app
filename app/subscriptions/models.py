from django.db import models
from utils.models import BaseModel
import stripe
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

stripe.api_key = settings.STRIPE_SECRET_KEY


class Plans(BaseModel):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Nome do plano",
        help_text="Nome do plano"
    )
    monthly_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço mensal",
        help_text="Preço mensal"
    )
    description = models.TextField(
        verbose_name="Descrição",
        help_text="Descrição"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Ativo",
        help_text="Ativo"
    )
    stripe_subscription_id = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
    stripe_price_id = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    next_due_date = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Assinatura | {self.name}"

    class Meta:
        verbose_name = "Plano"
        verbose_name_plural = "Planos"
        ordering = ["-created_at"]


class Products(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name="Nome do produto",
        help_text="Nome do produto"
    )
    description = models.TextField(
        verbose_name="Descrição",
        help_text="Descrição"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Preço",
        help_text="Preço"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Ativo",
        help_text="Ativo"
    )

    def __str__(self):
        return f"Produto | {self.name}"

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["-created_at"]


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=255, unique=True)
    stripe_price_id = models.CharField(max_length=255)
    next_due_date = models.DateTimeField()

    def __str__(self):
        return f"Subscription | {self.user.email} | {self.plan.name}"


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    stripe_transaction_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Transaction | {self.user.email} | {self.amount} {self.currency}"


@receiver(post_save, sender=Plans)
def create_or_update_stripe_plan(sender, instance, created, **kwargs):
    if created:
        product = stripe.Product.create(
            id=str(instance.id),
            name=instance.name,
            description=instance.description,
            active=instance.is_active,
        )
        price = stripe.Price.create(
            product=product.id,
            unit_amount=int(instance.monthly_price * 100),
            currency='brl',
            recurring={"interval": "month"},
        )
        instance.stripe_price_id = price.id
        instance.save()

    else:
        stripe.Product.modify(
            str(instance.id),
            name=instance.name,
            description=instance.description,
            active=instance.is_active,
        )
        # Atualizar o preço não é suportado diretamente, então você pode precisar criar um novo preço e desativar o antigo

# TODO: Ver por que nao consigo deletar um plano no stripe
# @receiver(post_delete, sender=Plans)
# def delete_stripe_plan(sender, instance, **kwargs):
#     stripe.Product.delete(str(instance.id))


@receiver(post_save, sender=Products)
def create_or_update_stripe_product(sender, instance, created, **kwargs):
    if created:
        product = stripe.Product.create(
            id=str(instance.id),
            name=instance.name,
            description=instance.description,
            active=instance.is_active,
        )
        price = stripe.Price.create(
            product=product.id,
            unit_amount=int(instance.price * 100),
            currency='brl',
        )
    else:
        stripe.Product.modify(
            str(instance.id),
            name=instance.name,
            description=instance.description,
            active=instance.is_active,
        )
        # Atualizar o preço não é suportado diretamente, então você pode precisar criar um novo preço e desativar o antigo


# TODO: Ver por que nao consigo deletar um produto no stripe
# @receiver(post_delete, sender=Products)
# def delete_stripe_product(sender, instance, **kwargs):
#     stripe.Product.delete(str(instance.id))


@receiver(post_save, sender=Subscription)
def create_or_update_stripe_subscription(sender, instance, created, **kwargs):
    if created:
        subscription = stripe.Subscription.create(
            customer=instance.user.stripeCustomerId,
            items=[{'price': instance.plan.stripe_price_id}],
        )
        instance.stripe_subscription_id = subscription.id
        instance.stripe_price_id = instance.plan.stripe_price_id
        instance.next_due_date = datetime.fromtimestamp(
            subscription.current_period_end)
        instance.save()
    else:
        # Atualizar a assinatura no Stripe se necessário
        pass
