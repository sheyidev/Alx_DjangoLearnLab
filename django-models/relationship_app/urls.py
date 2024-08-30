from django.urls import path
from .views import list_books, LibraryDetailView
from django.views.generic import TemplateView
from relationship_app.views import SignUpView, register
from django.urls import path, include

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/',LibraryDetailView.as_view(), name="library_view" ),
     path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',TemplateView.as_view(template_name='accounts/profile.html'),
             name='profile'),
     path("signup/", SignUpView.as_view(), name="templates/registration/signup"),
      path('register/', register, name="templates/register"),
]