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
from .test_func import is_admin, is_member, is_librarian
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

def admin_view(user):
     return user.is_authenticated and user.userprofile.role == "Admin"
    
@login_required
#@permission_required
#@user_passes_test(admin_view)
@user_passes_test(is_ddmin)
def admin_dashboard(request):
        return render(request, 'admin_view')


#class AdminView(TemplateView):
  #  template_name = 'admin_view.html'
#    role_required = 'Admin'

def librarian_check(user):
     return user.is_authenticated and user.userprofile.role == "librarian"
def member_check(user):
     return user.is_authenticated and user.userprofile.role == "Member"

@login_required
@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'librarian_view')

@login_required
@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, 'member_view')