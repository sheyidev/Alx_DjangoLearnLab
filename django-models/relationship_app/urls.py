from django.urls import path
from . import views
from django.views.generic import TemplateView
from relationship_app.views import SignUpView, register
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/',views.LibraryDetailView.as_view(), name="library_view" ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',TemplateView.as_view(template_name='accounts/profile.html'),
             name='profile'),
    path("signup/", SignUpView.as_view(), name="templates/registration/signup"),
    path('register/', views.register, name="templates/register"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),  # Logout view
]