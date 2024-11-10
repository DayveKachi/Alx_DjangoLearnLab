#python command
from bookshelf.models import Book
book = Book.objects.get(id=1);
book.title = "Nineteen Eighty-Four";
book.save();
print(book)

#expected output
#<QuerySet [<Book: Nineteen Eighty-Four George Orwell 1949>]>