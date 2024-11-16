CREATE command:

from bookshelf.models import Book
Book.objects.create(title="New book.", author="Dayve", publication_year=1998)
#This creates a new Book object with the given details.

RETRIEVE command:

from bookshelf.models import Book
a_book = Book.objects.get(title="New book.")
#This retrieves the book with the title "New book." from our database and stores it
#in the variable a_book

UPDATE command:

from bookshelf.models import Book
a_book = Book.objects.get(title="New book.")
a_book.title = "New title."
#This retrieves a Book with the title "New book." and updates the title to "New title."

DELETE command:

from bookshelf.models import Book
a_book = Book.objects.get(title="New book.")
a_book.delete()
#This retrieves a Book object with the title "New book." 
#Then it deletes it from the database