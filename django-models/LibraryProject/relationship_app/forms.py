from django import forms
from .models import Book

class BookCreationForm(forms.ModelForm):
    """Generates a form for creating a Book object"""
    class Meta:
        model = Book
        fields = ("title", "author")
        labels = {
            "title": "Title",
            "author": "Author",
        }
    