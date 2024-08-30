from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Library, Book
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
## create a function-based view
def list_books(request):
      books = Book.objects.all()
      
      return render(request, 'relationship_app/list_books.html',{'books':books} )

##Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.


class LibraryDetailView(DetailView):
      model = Library
      context_object_name = 'library_view'
      template_name = 'relationship_app/library_details.html'

     # def get_template_names(self):
        # Get the template name from the query parameters or use a default
       # template_name = self.kwargs.get('template_name', 'relationship_app/library_detail.html')
       # return [template_name]


# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            return redirect('profile')  # Redirect to the profile page or another page
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"
