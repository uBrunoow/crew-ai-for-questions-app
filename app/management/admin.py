# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User
from .forms import AdminPasswordChangeForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "is_superuser", "phone",
                    "description", "is_active", "reset_password_link", "stripeCustomerId",
                    "stripeSubscriptionId", "stripeSubscriptionStatus", "stripePriceId"]
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'created_at',
        'updated_at',
    )

    raw_id_fields = ('groups', 'user_permissions')
    search_fields = ('name',)
    date_hierarchy = 'created_at'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

    def get_fieldsets(self, request, obj=None):
        if obj:
            return [(None, {"fields": ("name", "email", "phone", "description",
                                       "is_active", 'is_superuser', 'is_staff')})]
        return [
            (None, {"fields": ("name", "email", 'password', "phone",
                               "description",
                               "is_active", 'is_superuser', 'is_staff')})
        ]

    def save_model(self, request, obj, form, change):
        if "password" in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

    def reset_password_link(self, obj):
        return format_html('<a href="{}">Redefinir senha</a>', reverse('admin:reset_password', args=[obj.id]))
    reset_password_link.short_description = 'Redefinir senha'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('reset-password/<int:user_id>/',
                 self.admin_site.admin_view(self.reset_password_view), name='reset_password'),
        ]
        return custom_urls + urls

    def reset_password_view(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.method == 'POST':
            form = AdminPasswordChangeForm(request.POST)
            if form.is_valid():
                new_password = form.cleaned_data['new_password']
                user.password = make_password(new_password)
                user.save()
                messages.success(request, 'Senha alterada com sucesso.')
                return redirect(reverse('admin:management_user_changelist'))
        else:
            form = AdminPasswordChangeForm()

        admin_form = admin.helpers.AdminForm(
            form,
            [(None, {'fields': ['new_password', 'confirm_password']})],
            {},
            model_admin=self
        )

        context = {
            'title': 'Redefinir senha',
            'adminform': admin_form,
            'form_url': request.get_full_path(),
            'opts': self.model._meta,
            'original': user,
            'save_as': False,
            'has_view_permission': self.has_view_permission(request, user),
            'has_add_permission': self.has_add_permission(request),
            'has_change_permission': self.has_change_permission(request, user),
            'has_delete_permission': self.has_delete_permission(request, user),
            'has_editable_inline_admin_formsets': False,
            'add': False,
            'change': True,
            'is_popup': False,
            'save_on_top': self.save_on_top,
        }

        return render(request, 'admin/change_form.html', context)
