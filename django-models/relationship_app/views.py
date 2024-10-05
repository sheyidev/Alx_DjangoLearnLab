from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class libraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library_view'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.object  # Get the current library object
        context['books'] = library.books.all()  # Retrieve all books associated with the library
        return context
 
    