from django.urls import path
from relationship_app.views import list_books
from relationship_app.views import libraryDetailView
urlpatterns = [
      path('home/', list_books,name='list_books'),
      path("library/<int:pk>/", libraryDetailView.as_view(),name="library_detail"),
]