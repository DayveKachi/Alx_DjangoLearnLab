from django.db import models
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    ADMIN = "ADM"
    LIBRARIAN = "LIB"
    MEMBER = "MEM"

    ROLE_CHOICES = (
        (ADMIN, "Admin"),
        (LIBRARIAN, "Librarian"),
        (MEMBER, "Member"),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default=MEMBER)
    
    def __str__(self):
        return f"{self.user.username} Profile"

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Author: {self.name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    class Meta:
        permissions = (
            ("can_add_book", "can create a book instance."),
            ("can_change_book", "can edit a book instance"),
            ("can_delete_book", "can delete a book instance"),
        )

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="libraries")

    class Meta:
        verbose_name_plural = "Libraries"
    
    def __str__(self):
        return f"Library: {self.name}"


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, Librarian of {self.library}"
