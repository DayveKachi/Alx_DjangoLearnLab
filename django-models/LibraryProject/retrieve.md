command:

from bookshelf.models import Book
a_book = Book.objects.get(title="New book.")

#This retrieves the book with the title "New book." from our database and stores it
#in the variable a_book