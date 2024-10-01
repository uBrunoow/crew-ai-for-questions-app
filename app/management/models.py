from django.db import models
from cuser.models import AbstractCUser
import stripe
from django.conf import settings
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
# Create your models here.

stripe.api_key = settings.STRIPE_SECRET_KEY


class User(AbstractCUser):
    name = models.CharField(
        max_length=100, help_text="Nome do usuário", verbose_name="Nome"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, null=True, blank=True
    )
    phone = models.CharField(
        max_length=15, verbose_name="Phone", help_text="Telefone do usuário"
    )
    description = models.TextField(
        verbose_name="Description", help_text="Descrição do usuário"
    )
    is_active = models.BooleanField(
        default=True, help_text="Usuário ativo", verbose_name="Ativo"
    )
    stripeCustomerId = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Stripe Customer ID"
    )
    stripeSubscriptionId = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Stripe Subscription ID"
    )
    stripeSubscriptionStatus = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Stripe Subscription Status"
    )
    stripePriceId = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Stripe Price ID"
    )

    class Meta(AbstractCUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def save(self, **kwargs) -> None:
        return super().save(**kwargs)

    def __str__(self):
        if self.first_name and self.last_name:
            return self.email + " | " + self.first_name + " " + self.last_name
        return self.email


@receiver(post_save, sender=User)
def create_or_update_stripe_customer(sender, instance, created, **kwargs):
    if created:
        # Cria o cliente no Stripe
        customer = stripe.Customer.create(
            id=str(instance.id),
            name=instance.name,
            email=instance.email,
        )

        # ID do plano "FREE" no Stripe
        # Substitua pelo ID real do plano "FREE"
        free_plan_id = settings.STRIPE_FREE_PRICE_ID

        # Cria a assinatura para o plano "FREE"
        subscription = stripe.Subscription.create(
            customer=customer.id,
            items=[{'price': free_plan_id}],
        )

        # Atualiza o usuário com as informações do Stripe
        instance.stripeCustomerId = customer.id
        instance.stripeSubscriptionId = subscription.id
        instance.stripeSubscriptionStatus = subscription.status
        instance.stripePriceId = free_plan_id
        instance.save()
    else:
        # Atualiza o cliente no Stripe
        stripe.Customer.modify(
            str(instance.id),
            name=instance.name,
            email=instance.email,
        )


@receiver(pre_delete, sender=User)
def delete_stripe_customer(sender, instance, **kwargs):
    if instance.stripeCustomerId:
        try:
            stripe.Customer.delete(instance.stripeCustomerId)
        except stripe.error.StripeError as e:
            print(f"Error deleting Stripe customer: {e}")
