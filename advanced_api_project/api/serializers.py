from rest_framework import serializers
from .models import Author, Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    """This serializer serializes the data for the Book model
    and also validates that the publication year is not in the future"""

    class Meta:
        model = Book
        fields = ("title", "publication_year", "author")

    def validate(self, data):
        current_year = date.today().year
        if data["publication_year"] > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future"
            )
        return data


class AuthorSerializer(serializers.ModelSerializer):
    """This serializer serializes the data for the Author model
    and has a nested serializer field to serialize related books dynamically"""

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ("name", "books")
