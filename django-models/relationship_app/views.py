from typing import Any
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from  relationship_app.query_samples import list_all_books_in_library
from .models import Library, Book
from django.utils import timezone
# Create your views here.
## create a function-based view
def list_all_books_in_database(request):
      books = Book.objects.all()
      #return HttpResponse({books.title, books.author})
      return render(request, 'relationship_app/list_books.html',{'books':books} )

##Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.


class LibraryDisplayView(DetailView):
      model = Library
      #context_object_name = 'library_view' # Name of the context object in the template
      template_name = 'relationship_app/library_detail.html'

     # def get_template_names(self):
        # Get the template name from the query parameters or use a default
       # template_name = self.kwargs.get('template_name', 'relationship_app/library_detail.html')
       # return [template_name]

"""

      def get_queryset(self):
        # Retrieve the library name from URL parameters
        library_name = self.kwargs.get('name')  # Adjust according to URL pattern
        # Use the function to get books for the specified library
        return list_all_books_in_library(library_name)

      def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         library_name = self.kwargs.get('name')
         library = get_object_or_404(Library, name=library_name)
         context['library'] = library
         return context
 
    

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
  

"""