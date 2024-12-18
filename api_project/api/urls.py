from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r"books_all", BookViewSet, basename="book_all")

urlpatterns = [
    path("api/token/", obtain_auth_token, name="obtain_auth_token"),
    path("books/", BookList.as_view(), name="book-list"),  # Maps to the BookList view
    path("", include(router.urls)),
]
