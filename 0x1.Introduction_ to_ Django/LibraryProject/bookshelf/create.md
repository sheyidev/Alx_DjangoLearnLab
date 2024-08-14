from bookshelf.models import Book

//new_book = Book(title='New Book', author='Jane Smith', publication_year=2024)

newbook = Book.objects.create(
    title='1984', author='George Orwell', publication_year=1949)

