from django.contrib import admin
from .models import Librarian, Library, Author, Book, UserProfile

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)
