from django.db import models

# Create your models here.


class Book(models.Model):
    """Defines the attributes for the Book model."""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=True, blank=True)
