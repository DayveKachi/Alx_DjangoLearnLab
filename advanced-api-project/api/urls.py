# from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    BookListView,
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
)

# router = DefaultRouter()

urlpatterns = [
    path("books/", BookListView.as_view(), name="books_list"),
    path("books/create/", BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("books/update/<int:pk>/", BookUpdateView.as_view(), name="book_update"),
    path("books/delete/<int:pk>/", BookDeleteView.as_view(), name="book_delete"),
    path("token/", obtain_auth_token, name="obtain_token"),
]

# urlpatterns += router.urls
