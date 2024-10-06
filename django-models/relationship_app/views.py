from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .roles_based import is_admin, is_librarian, is_member
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .forms import BookForm

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