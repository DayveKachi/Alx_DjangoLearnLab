from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path("register/"),
    path("login/"),
    path("profile/"),
]

if settings.DEBUG:  # Serve media files only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
