from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


# Serializer for the Post model
class PostSerializer(serializers.ModelSerializer):
    # Nested author information can be returned if needed
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )

    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "created_at", "updated_at"]

    def validate_title(self, value):
        """Ensure that title is unique"""
        if Post.objects.filter(title=value).exists():
            raise serializers.ValidationError("A post with this title already exists.")
        return value

    def create(self, validated_data):
        """Automatically assign the author when creating a post"""
        if "author" not in validated_data:
            validated_data["author"] = self.context[
                "request"
            ].user  # Get the user from the request
        return super().create(validated_data)


# Serializer for the Comment model
class CommentSerializer(serializers.ModelSerializer):
    # Nested author and post information can be returned if needed
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), required=False
    )

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["author", "created_at", "updated_at"]

    def validate_content(self, value):
        """Validate comment content"""
        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "Comment content must be at least 10 characters long."
            )
        return value

    def create(self, validated_data):
        """Automatically assign the post and author when creating a comment"""
        if "author" not in validated_data:
            validated_data["author"] = self.context[
                "request"
            ].user  # Get the logged-in user from the request
        if "post" not in validated_data:
            raise serializers.ValidationError("Post is required for a comment.")
        return super().create(validated_data)
