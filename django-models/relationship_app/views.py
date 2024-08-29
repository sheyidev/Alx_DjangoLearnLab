from django.shortcuts import render
from django.http import HttpResponse
from .models import Library, Book
# Create your views here.
## create a function-based view
def list_all_books_in_database(request):
      books = Book.objects.all()
      #return HttpResponse({books.title, books.author})
      return render(request, 'relationship_app/list_books.html',{'books':books} )