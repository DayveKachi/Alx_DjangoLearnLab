from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserRegistrationView,
    UserProfileView,
    UnFollowUserView,
    FollowUserView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),  # DRF built-in token view
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow_user"),
    path("unfollow/<int:user_id>/", UnFollowUserView.as_view(), name="unfollow_user"),
]
