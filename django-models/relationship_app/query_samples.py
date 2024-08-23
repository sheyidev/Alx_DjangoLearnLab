# query_samples.py

from relationship_app.models import Author, Book, Library

def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    try:
        # Get the author object with the given name
        author = Author.objects.get(filter=author_name)
        # Get all books by the author using the related_name 'books'
        books = author.books.all()
        print(f"Books by {author_name}: {[book.title for book in books]}")
    except Author.DoesNotExist:
        print(f"No author found with the name: {author_name}")


def list_all_books_in_library(library_name):
    """
    List all books in a specific library.
    """
    try:
        # Get the library object with the given name
        library = Library.objects.get(name=library_name)
        # Get all books in the library using the related_name 'libraries'
        books = library.books.all()
        print(f"Books in the {library_name} library: {[book.title for book in books]}")
    except Library.DoesNotExist:
        print(f"No library found with the name: {library_name}")


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a specific library.
    """
    try:
        # Get the library object with the given name
        library = Library.objects.get(name=library_name)
        # Access the librarian field directly
        librarian = library.librarian
        print(f"The librarian for the {library_name} library is: {librarian}")
    except Library.DoesNotExist:
        print(f"No library found with the name: {library_name}")


# Example usage of the functions
if __name__ == "__main__":
# query_books_by_author("J.K. Rowling")
#list_all_books_in_library("Central Library")
#retrieve_librarian_for_library("Central Library")