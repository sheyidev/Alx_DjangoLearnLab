from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login

# Create your views here.
def list_books(request):
    """
    A function-based view to list all books with their titles and authors.
    """
    books = Book.objects.all()  ## Retrieve all book objects from the database
    context = {'books': books}  # # Pass the books to the template context
    return render(request, 'relationship_app/list_books.html', context)


from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    """
    A class-based view to display details of a specific library, including all books.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'relationship_app/register.html', {'form': form})

## DOING THE SAME thing as above
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})
