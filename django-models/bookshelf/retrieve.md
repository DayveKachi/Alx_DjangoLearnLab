#python command
from bookshelf.models import Book
#retrieve all books
books = Book.objects.all();

#retrieve a single book using id
book = Book.objects.get(id=1)
print(books);
print(book)

#expected output
#<QuerySet [<Book: 1984 George Orwell 1949>]>