#!/bin/python
from relationship_app.models import Author,Book, Librarian, Library

def get_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.get(author=author)
        return books 

    except Author.DoesNotExist:
        return None

def list_all_books_in_a_lib(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return None 
    
def librarian_from_a_lib(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Librarian.DoesNotExist, Library.DoesNotExist):
        return None 