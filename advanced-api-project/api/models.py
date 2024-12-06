from django.db import models


class Author(models.Model):
    """This model outlines the attributes of an Author"""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    """This model outlines the attributes of a Book and its relationship with the Author model"""

    title = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=None)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
