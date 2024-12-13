from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Info",
            {
                "fields": ("bio", "profile_picture", "followers"),
            },
        ),
    )
    list_display = ("username", "email", "bio", "profile_picture")
