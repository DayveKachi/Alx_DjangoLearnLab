from django.urls import path, include
from .views import (
    book_list_view,
    LibraryDetailView,
    RegistrationView,
    create_book,
    update_book,
    delete_book,
    Admin,
    Librarian,
    Member,
)

app_name = "relationship_app"

urlpatterns = [
    path("", book_list_view, name="list_books"),
    path("library/<int:pk>/books", LibraryDetailView.as_view(), name="library_detail"),
    path("accounts/register/", RegistrationView.as_view(), name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("role/admin/", Admin, name="admin_role"),
    path("role/librarian/", Librarian, name="librarian_role"),
    path("role/member/", Member, name="member_role"),
    path("add_book/", create_book, name="create_book"),
    path("edit_book/<int:pk>/", update_book, name="update_book"),
    path("delete_book/<int:pk>/", delete_book, name="delete_book"),
]
