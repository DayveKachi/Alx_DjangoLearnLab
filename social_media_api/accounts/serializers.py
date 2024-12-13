from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password", "token"]

    def create(self, validated_data):
        # Create a new user and generate their token
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        Token.objects.create(user=user)
        return user

    def get_token(self, obj):
        # Fetch the token for the created user
        token = Token.objects.get(user=obj)
        return token.key


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "bio", "profile_picture"]
