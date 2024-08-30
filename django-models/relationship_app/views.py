from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Library, Book
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegistrationForm

# Create your views here.
## create a function-based view
def list_books(request):
      books = Book.objects.all()
      
      return render(request, 'list_books.html',{'books':books} )

##Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.


class LibraryDetailView(DetailView):
      model = Library
      context_object_name = 'library_view'
      template_name = 'relationship/library_details.html'

## create a user registration form in form.py and reference it in the registration view here
class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

"""
For User registration, is either i use Createview class that does a lot of stuff lile validity
or use a function like below
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            return redirect('profile')  # Redirect to the profile page or another page
    else:
        form = RegistrationForm()
    return render(request, 'registration/accounts/register.html', {'form': form})

"""

