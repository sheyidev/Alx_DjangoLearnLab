from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from  relationship_app.query_samples import list_all_books_in_libarary
from .models import Library, Book
from django.utils import timezone
# Create your views here.
## create a function-based view
def list_all_books_in_database(request):
      books = Book.objects.all()
      #return HttpResponse({books.title, books.author})
      return render(request, 'relationship_app/list_books.html',{'books':books} )

##Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
class LibraryDisplayView(ListView):
      model = Library
      context_object_name = 'library_view' # Name of the context object in the template
      template_name = 'relationship_app/library_detail.html'
 
    
"""
      def get_queryset(self):
        # Retrieve the library object based on the URL parameter
        library_id = self.kwargs.get('pk')
        library = get_object_or_404(Library, id=library_id)
        
        # Return books related to the specified library
        return library.books.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library_id = self.kwargs.get('pk')
        library = get_object_or_404(Library, id=library_id)
        context['library'] = library
        return context  
"""