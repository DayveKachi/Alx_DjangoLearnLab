from django.urls import path, include
from .views import (
    book_list_view,
    LibraryDetailView,
    RegistrationView,
    create_book,
    update_book,
    delete_book,
    admin_view,
    librarian_view,
    member_view,
)

app_name = "relationship_app"

urlpatterns = [
    path("", book_list_view, name="list_books"),
    path("library/<int:pk>/books", LibraryDetailView.as_view(), name="library_detail"),
    path("accounts/register/", RegistrationView.as_view(), name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin_view/", admin_view, name="admin_view"),
    path("librarian_view/", librarian_view, name="librarian_view"),
    path("member_view/", member_view, name="member_view"),
    path("add_book/", create_book, name="create_book"),
    path("edit_book/<int:pk>/", update_book, name="update_book"),
    path("delete_book/<int:pk>/", delete_book, name="delete_book"),
]
