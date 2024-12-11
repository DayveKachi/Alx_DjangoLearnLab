from django.urls import path
from .views import (
    HomeView,
    UserCreateView,
    edit_profile,
    PostCreateView,
    PostDeleteView,
    post_detail,
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
    path(
        "posts/<int:post_id>/comments/new",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
    path(
        "posts/<int:post_id>/comments/<int:comment_id>/",
        CommentDetailView.as_view(),
        name="comment_detail",
    ),
    path(
        "post/<int:post_id>/comments/<int:comment_id>/update/",
        CommentUpdateView.as_view(),
        name="comment_update",
    ),
    path(
        "post/<int:post_id>/comments/<int:comment_id>/delete/",
        CommentDeleteView.as_view(),
        name="comment_delete",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
