#create
#python command

from bookshelf.models import Book
new_book = Book(title=1984, author="George Orwell", publication_year=1949);

new_book.save();

#expected output
No error message indicating the instance was successfully created.

#retrieve
#python command
from bookshelf.models import Book
books = Book.objects.all();
print(books);

#expected output
#<QuerySet [<Book: 1984 George Orwell 1949>]>

#update
#python command
from bookshelf.models import Book
book = Book.objects.get(id=1);
book.title = "Nineteen Eighty-Four";
book.save();
print(book)

#expected output
#<QuerySet [<Book: Nineteen Eighty-Four George Orwell 1949>]>

#delete
#python command
from bookshelf.models import Book

book = Book.objects.get(id=1);
book.delete();

#expected output
the book record will be deleted
