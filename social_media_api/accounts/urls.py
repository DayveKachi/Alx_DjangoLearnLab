from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegistrationView, UserProfileView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),  # DRF built-in token view
    path("profile/", UserProfileView.as_view(), name="profile"),
]

if settings.DEBUG:  # Serve media files only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
