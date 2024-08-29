"""
Prepare a Python script query_samples.py in the relationship_app directory. This script should contain the query for each of the following of relationship:
Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.

"""
from .models import Book, Author, Library,Librarian
##query all the books first from the Book class
books = Book.objects.all()


## filter by author becuase of the instance
books_by_author = Book.objects.filter(author='author')

## list all books in library

## first get the library instance
library = Library.objects.get(name='name')

books_in_library = books.objects.all()

## Liberian for a libary
## get the librarry instance first
library_instance = Library.objects.get(library='library_name')

##use the lib instance to search for the liberian for the lib
"""
Accessing Librarian from Library:

Since you want to find the librarian for a given library, you should start with the Library instance and use the related_name defined in the OneToOneField to access the associated Librarian.
"""
liberian = library_instance.liberian.get()

"""
The OneToOneField creates a reverse relationship which allows you to navigate from Librarian to Library. However, if your starting point is the Library, you should follow the relationship from Library to Librarian.
"""
