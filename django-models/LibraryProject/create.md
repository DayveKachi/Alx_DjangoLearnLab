command:

from bookshelf.models import Book
Book.objects.create(title="New book.", author="Dayve", publication_year=1998)

#This creates a new Book object with the given details.