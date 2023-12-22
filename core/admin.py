from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_superuser', )
    list_filter = ('is_staff', )
    search_fields = ("email", )
    ordering = ("email", )
    filter_horizontal = ()

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", ),
            },
        ),
    )
