# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Plans, Products, Subscription, Transaction


@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'name',
        'monthly_price',
        'description',
        'is_active',
        'stripe_subscription_id',
        'stripe_price_id',
        'next_due_date',
    )
    list_filter = ('created_at', 'updated_at', 'is_active', 'next_due_date')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'name',
        'description',
        'price',
        'is_active',
    )
    list_filter = ('created_at', 'updated_at', 'is_active')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'plan',
        'stripe_subscription_id',
        'stripe_price_id',
        'next_due_date',
    )
    list_filter = ('user', 'plan', 'next_due_date')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'stripe_transaction_id',
        'amount',
        'currency',
        'status',
        'created_at',
    )
    list_filter = ('user', 'created_at')
    date_hierarchy = 'created_at'
