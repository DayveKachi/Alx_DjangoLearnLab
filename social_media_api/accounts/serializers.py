from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "bio",
            "profile_picture",
            "followers",
            "following",
        )
        read_only_fields = ("followers", "following")
