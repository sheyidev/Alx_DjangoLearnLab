from .models import Book, Author, Library,Librarian

"""
Prepare a Python script query_samples.py in the relationship_app directory. This script should contain the query for each of the following of relationship:
Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.

"""

def query_by_author(author_name):
##query all the books first from the Book class
    #books = Book.objects.all()

    ## get the author object with the given name
    author = Author.objects.get(name=author_name)
    ## filter books by author based on author the instance
    books = Book.objects.filter(author=author)
    books= author.books.all()

def list_all_books_in_library(library_name):
    ## list all books in library

    ## first get the library instance
    library = Library.objects.get(name=library_name)
    
# Get all books in the library using the related_name 'libraries'
    #librarian = Librarian.objects.get(library=library)
   # books_in_the_lib = Librarian.objects.get(library=library)

    #books_in_library = Book.objects.all()
    books_in_library = library.books.all()

def retrieve_liberian_from_library(library_name):
    ## Liberian for a libary
    ## get the librarry instance first
    library_instance = Library.objects.get(name=library_name)

    ##use the lib instance to search for the liberian for the lib
    ##Accessing Librarian from Library:
    ##Since you want to find the librarian for a given library, you should start with the Library instance and use the related_name defined in the OneToOneField to access the associated Librarian.

    librarian = library_instance.librarian.get(library=library_instance)
    ##The OneToOneField creates a reverse relationship which allows you to navigate from Librarian to Library. However, if your starting point is the Library, you should follow the relationship from Library to Librarian.
    
