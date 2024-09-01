from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from .test_func import is_librarian
# define the views here
@user_passes_test(is_librarian)
def librarian_only_view(request):
    return HttpResponse("This view is for Librarians only.")