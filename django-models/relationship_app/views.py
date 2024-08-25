from django.shortcuts import render
from .models import Book


# Create your views here.
def list_all_books(request):
    """
    A function-based view to list all books with their titles and authors.
    """
    books = Book.objects.all()  ## Retrieve all book objects from the database
    context = {'books': books}  # # Pass the books to the template context
    return render(request, 'relationship_app/book_list.html', context)
