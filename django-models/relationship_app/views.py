from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Library, Book, UserProfile
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from  .test_func import is_admin, is_librarian, is_member
#from .decorators import permission_required


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
     return render(request, 'relationship_app/admin_view')

@user_passes_test(is_member)
def member_view(request):
     return render(request, 'relationship_app/member_view')

@user_passes_test(is_librarian)
def library_view(request):
     return render(request, 'relationship_app/librarian_view')