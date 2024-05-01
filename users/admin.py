from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from django.utils.translation import gettext_lazy as _


User = get_user_model()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "last_login",
        "is_superuser",
        "date_joined",
        "is_staff",
        "is_active",

    )
    list_filter = (
        "last_login",
        "is_superuser",
        "date_joined",
        "is_staff",
        "is_active",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    ordering = ("email",)
    fieldsets = (
        (
            _("Personal Info"),
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (_("Permissions Info"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login",)}),
        ("Password Info", {"fields": ("password",)}),
    )
    add_fieldsets = (
        (
            _("Personal Info"),
            {"fields": ("email", "first_name", "last_name")},
        ),
        (_("Permissions Info"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login",)}),
        ("Password Info", {"fields": ("password1", "password2")}),
    )
