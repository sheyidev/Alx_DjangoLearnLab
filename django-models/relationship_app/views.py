from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


def home_view(request):
    return render(request,'relationship_app/home.html')  # 'home.html' is the template name

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library_view'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.object  # Get the current library object
        context['books'] = library.books.all()  # Retrieve all books associated with the library
        return context
    

#class SignUpView(CreateView):

 #   form_class = UserCreationForm
 #   success_url = reverse_lazy('login')
 #   template_name = 'registration/register.html'

def register(request):
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               user = form.save()
               login(request, user)
               return redirect('login')
     else:
        form = UserCreationForm()
     return render(request, 'relationship_app/register.html', {'form': form})
     
    
class CustomerLoginView(LoginView):
    template_name = 'relationship_app/login.html'  # Custom login template
    redirect_authenticated_user = False  # Redirect if already logged in
    success_url = reverse_lazy('list_books')
    def get_success_url(self):
        return reverse_lazy('list_books')  # Redirect to the URL mapped to the name 'home'