from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    CommentViewSet,
    FeedListView,
    LikePostView,
    UnlikePostView,
)

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path(
        "", include(router.urls)
    ),  # Automatically includes the routes for the viewsets
    path("feed/", FeedListView.as_view(), name="feed"),
    path("post/<int:pk>/like/", LikePostView.as_view(), name="like_post"),
    path("post/<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike_post"),
]
