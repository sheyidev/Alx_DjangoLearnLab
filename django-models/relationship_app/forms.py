# relationship_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#class SignUpForm(UserCreationForm):
  #  class Meta:
  #      model = User
   #     fields = ['username', 'password1', 'password2']
class RegistrationForm(UserCreationForm):
     email = forms.EmailField(required=True)

     class Meta:
          model = User
          fields = ['username', 'email', 'password1', 'password2']