from django.urls import path
from .views import list_books
from .views import libraryDetailView
urlpatterns = [
      path('home/', list_books,name='list_books'),
      path("library/<int:pk>/", libraryDetailView.as_view(),name="library_detail"),
]