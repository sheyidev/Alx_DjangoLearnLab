from models import Author, Book, Library, Librarian

"""
 Implement Sample Queries:
    - Prepare a Python script `query_samples.py` in the `relationship_app` directory. This script should contain the query for each of the following of relationship:
       - Query all books by a specific author.
       - List all books in a library.
       - Retrieve the librarian for a library.
"""
## filter books by author
def query_books_by_author(author_name):
    
  try:
    books_by_author = Author.objects.get(name=author_name)
    # Filter books by the author object
    books = Book.objects.filter(author=books_by_author)

  except Author.DoesNotExist:
     print(f"No author found with the name: {author_name}")

def list_all_the_books(all_books):
    books = Book.objects.all()

def retrieve_librarian_from_a_lib(librarian_name):
     Librarian = Book.objects.filter()