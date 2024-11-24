from django.db import models

# Create your models here.


class Book(models.Model):
    """Defines the atributes for a book instance"""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title[50]
