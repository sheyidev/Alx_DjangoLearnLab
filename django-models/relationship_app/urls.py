from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import CustomerLoginView, home_view
from django.contrib.auth.views import LogoutView
#from .views import SignUpView
from relationship_app import views
from .views import admin_view, member_view, library_view


urlpatterns = [
      path('home/', list_books,name='list_books'),
      path("library/<int:pk>/", LibraryDetailView.as_view(),name="library_detail"),
      path('login/', CustomerLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
     # path('signup/', SignUpView.as_view(template_name='registration/register.html'), name='signup'),
      path('signup/', views.register,  name='signup'),
      path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
      path('', home_view, name='home'),
]     


urlpatterns = [
   path('admin-view/', admin_view, name='admin_view'),
   path('member-view', member_view , name='member_view'),
   path('library-view', library_view, name='library_view'),
]