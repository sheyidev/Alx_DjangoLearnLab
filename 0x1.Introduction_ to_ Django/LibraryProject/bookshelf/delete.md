from bookshelf.models import Book



newbook = Book.objects.delete(
    title='1984', author='George Orwell', publication_year=1949)
