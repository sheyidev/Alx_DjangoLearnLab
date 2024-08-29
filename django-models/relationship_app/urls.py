from django.urls import path
from .views import list_books, LibraryDisplayView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/',LibraryDisplayView.get_template_names, name="library_view" )
]