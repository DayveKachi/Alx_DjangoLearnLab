from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a post or comment to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the post or comment.
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for performing CRUD operations on the Post model.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]  # Ensure users can only edit their own posts

    def perform_create(self, serializer):
        # Automatically set the author as the logged-in user
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for performing CRUD operations on the Comment model.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]  # Ensure users can only edit their own comments

    def perform_create(self, serializer):
        # Automatically set the author as the logged-in user
        post = serializer.validated_data.get("post")  # Ensure the post exists
        if not post:
            raise PermissionDenied("You must specify a post.")
        serializer.save(author=self.request.user, post=post)


class FeedListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
        return posts
