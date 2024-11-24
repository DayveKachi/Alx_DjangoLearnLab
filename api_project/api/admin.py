from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("title", "author")
    search_fields = ("title", "author")


admin.site.register(Book, BookAdmin)