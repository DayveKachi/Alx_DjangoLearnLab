from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView
from .models import Book, Library
from .forms import BookCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, user_passes_test


# Create your views here.


def book_list_view(request):
    """function-based view that lists all books stored in the database."""
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)


class LibraryDetailView(DetailView):
    """Class-based view that displays details for a specific library,
    listing all books available in that library."""

    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("relationship_app:login")


@permission_required("relationship_app.can_add_book")
def create_book(request):
    if request.method == "POST":
        form = BookCreationForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect(reverse("relationship_app:list_books"))
    else:
        form = BookCreationForm()

    context = {"form": form}
    return render(request, "relationship_app/create_book.html", context)


@permission_required("relationship_app.can_change_book")
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookCreationForm(instance=book, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect(reverse("relationship_app:list_books"))
    else:
        form = BookCreationForm(instance=book)

    context = {"form": form, "book": book}
    return render(request, "relationship_app/update_book.html", context)


@permission_required("relationship_app.can_delete_book")
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect(reverse("relationship_app:list_books"))
    else:
        context = {"book": book}
        return render(request, "relationship_app/delete_book.html", context)


# Admin, Librarian and Member Views


def admin_check(user):
    return user.profile.role == "Admin"


@user_passes_test(admin_check)
def Admin(request):
    return HttpResponse("<p>You are an Admin</p>")


def librarian_check(user):
    return user.profile.role == "Librarian"


@user_passes_test(librarian_check)
def Librarian(request):
    return HttpResponse("<p>You are a Librarian</p>")


def member_check(user):
    return user.profile.role == "Member"


@user_passes_test(member_check)
def Member(request):
    return HttpResponse("<p>You are a Member</p>")
