from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import CustomerLoginView, home_view
from django.contrib.auth.views import LogoutView
#from .views import SignUpView
from relationship_app import views
from .views import admin_view, member_view, library_view, logoutUser


urlpatterns = [
      path('home/', list_books,name='list_books'),
      path("library/<int:pk>/", LibraryDetailView.as_view(),name="library_detail"),
      path('login/', CustomerLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
     # path('signup/', SignUpView.as_view(template_name='registration/register.html'), name='signup'),
      path('logout/', views.logoutUser,  name='logout'),
      path('signup/', views.register,  name='signup'),
      path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
      path('', home_view, name='home'),
      path('add_book/', views.add_book, name='add_book'),
      path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
      path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
      path('admin-view/', admin_view, name='admin_view'),
      path('member-view', member_view , name='member_view'),
      path('library-view', library_view, name='library_view'),
] 
  

