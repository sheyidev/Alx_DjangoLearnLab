from django.urls import path
from .views import list_all_books_in_database

urlpatterns = [
    path('books/', list_all_books_in_database, name='list_books')
]