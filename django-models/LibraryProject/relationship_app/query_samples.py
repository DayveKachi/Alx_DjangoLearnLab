#This script contains the query for each of the following of relationship:
# 1. Query all books by a specific author.
# 2. List all books in a library.
# 3. Retrieve the librarian for a library.

from .models import Book, Library

def all_books_of_author(author):
    """Query all books by a specific author"""
    books = Book.objects.filter(author=author)
    return books

def all_books_in_library(library):
    """Query all books in a library"""
    choice_library = Library.objects.filter(name=library)
    lib_books = choice_library.books.all()
    return lib_books

def librarian(library):
    """Retrieve the librarian for a library"""
    choice_library = Library.objects.filter(name=library)
    librarian_name = choice_library.librarian.name
    return librarian_name

def main():
    """Runs defined database queries."""
    author = input("Please enter author's name to retrieve his books: ")
    author_books = all_books_of_author(author)
    print(f"Books written by {author} are: ", author_books)

    library1 = input("Please enter Library's name to retrieve all books in it: ")
    library_books = all_books_in_library(library1)
    print(f"Books in {library1} are: ", library_books)

    library2 = input("Please enter Library's name to retrieve its Librarian: ")
    librarian_name = librarian(library2)
    print(f"The Librarian for {library2} is: ", librarian_name)


if __name__ == "__main__":
    main()