#python command
from bookshelf.models import Book

book = Book.objects.get(id=1);
book.delete();

#expected output
the book record will be deleted