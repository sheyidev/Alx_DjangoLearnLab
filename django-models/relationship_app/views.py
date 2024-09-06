from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Library, Book, UserProfile
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from  .test_func import is_admin, is_librarian, is_member
from .forms import BookForm
from .models import Book
#from .decorators import permission_required
def home(request):
    return render(request, 'relationship_app/home.html')

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

## create a user registration form in form.py and reference it in the registration view here
class SignUpView(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

def register(request):
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid:
               user = form.save()
               login(request, user)
               redirect('login')
     else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
     


@user_passes_test(is_admin)
def admin_view(request):
     return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_member)
def member_view(request):
     return render(request, 'relationship_app/member_view.html')

@user_passes_test(is_librarian)
def library_view(request):
     return render(request, 'relationship_app/librarian_view.html')

## add the can_add_view with permission required criterai
@permission_required('relationship_app.can_add_book')
def add_book(request):
     if request.method == 'POST':
          form = BookForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('list_books')
     else:
          form = BookForm()
          return render(request, 'relationship_app/book_form.html', {'form': form})
     
@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
     if request.method == 'POST':
        book = get_object_or_404(Book, instance=book)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
     else:
        form = BookForm(instance=book)
     return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})