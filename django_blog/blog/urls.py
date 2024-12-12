from django.urls import path
from .views import (
    search_posts,
    edit_profile,
    post_detail,
    tag_posts_view,
    HomeView,
    UserCreateView,
    PostCreateView,
    PostDeleteView,
    PostListView,
    PostUpdateView,
    CommentCreateView,
    CommentUpdateView,
    CommentDetailView,
    CommentDeleteView,
)
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "register/",
        UserCreateView.as_view(template_name="blog/register.html"),
        name="register",
    ),
    path("profile/", edit_profile, name="edit_profile"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", post_detail, name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    # Create Comment
    path(
        "post/<int:pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
    # Update Comment
    path(
        "comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_update"
    ),
    # Delete Comment
    path(
        "comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"
    ),
    # Read Comment
    path(
        "posts/<int:post_id>/comments/<int:comment_id>/",
        CommentDetailView.as_view(),
        name="comment_detail",
    ),
    path("search/", search_posts, name="search_posts"),
    path("tags/<str:tag_name>/", tag_posts_view, name="tag_posts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
