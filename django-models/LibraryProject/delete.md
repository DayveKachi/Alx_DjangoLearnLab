command:

from bookshelf.models import Book
a_book = Book.objects.get(title="New book.")
a_book.delete()

#This retrieves a Book object with the title "New book." 
#Then it deletes it from the database