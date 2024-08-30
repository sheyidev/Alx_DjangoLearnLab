from django.urls import path
from . import views
from django.views.generic import TemplateView
from relationship_app.views import SignUpView
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/',views.LibraryDetailView.as_view(), name="library_view" ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',TemplateView.as_view(template_name='accounts/profile.html'),
             name='profile'),
    path("register/", SignUpView.as_view(), name="register"),
    #path('register/', views.register, name="templates/accounts/register"),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login view
    path('librarian/dashboard/', views.librarian_dashboard, name= 'librarian_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name= 'admin_dashboard'),
    path('member/dashboard/', views.member_dashboard, name= 'member_dashboard')
]