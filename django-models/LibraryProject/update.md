command:

from bookshelf.models import Book
a_book = Book.objects.get(title="New book.")
a_book.title = "New title."

#This retrieves a Book with the title "New book." and updates the title to "New title."