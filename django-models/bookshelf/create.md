#python command

from bookshelf.models import Book
new_book = Book.objects.create(title=1984, author="George Orwell", publication_year=1949);

new_book.save();

#expected output
No error message indicating the instance was successfully created.