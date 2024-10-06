from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import CustomerLoginView, home_view
from django.contrib.auth.views import LogoutView
from .views import SignUpView
from .views import register


urlpatterns = [
      path('home/', list_books,name='list_books'),
      path("library/<int:pk>/", LibraryDetailView.as_view(),name="library_detail"),
      path('login/', CustomerLoginView.as_view(template_name='registration/login.html'), name='login'),
     # path('signup/', SignUpView.as_view(template_name='registration/register.html'), name='signup'),
      path('signup/', register,  name='signup'),
      path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
      path('', home_view, name='home'),
]     