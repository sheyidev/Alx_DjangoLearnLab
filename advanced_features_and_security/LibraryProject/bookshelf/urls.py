from django.urls import path
from django.views.generic import TemplateView
from bookshelf.views import SignUpView
from django.urls import path, include


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
   # path('accounts/profile/',TemplateView.as_view(template_name='accounts/profile.html'),
             #name='profile'),
     path("signup/", SignUpView.as_view(), name="templates/registration/signup"),

]