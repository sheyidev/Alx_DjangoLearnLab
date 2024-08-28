"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, RegisterView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name='list_books'),  # URL pattern for the function-based view
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL pattern for the class-based view
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/', views.register, name='register'),  # Use the function-based view `register`
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view')
]