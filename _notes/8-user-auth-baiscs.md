## User Authentication Basics
This concept page introduces the basics of implementing user authentication in Django applications. 

It covers the built-in `authentication system`, `user registration`, `login and logout` functionalities, `user permissions and groups`, and various authentication-related components provided by Django.

## Concept Overview
### Topics
- **Django’s Built-in Authentication System**
- **User Registration**
- **User Login and Logout**
- **Password Management**
- **Authentication Views and URLs**


## Learning Objectives
- Understand the purpose and components of Django’s authentication system
- Learn how to register new users and create user accounts
- Implement user login and logout functionalities
- Manage user passwords securely
- Utilize Django’s built-in authentication views and URLs


## Django’s Built-in Authentication System

Django comes with a built-in authentication system that provides a set of `models`, `views`, and `utilities` for handling user authentication. Here’s a breakdown of the core components:

1. **User Model**

    The `User model` serves as the foundation for representing a user within the authentication system. It stores essential user information such as username, password (hashed for security), email address, and other relevant user-related data.
    
    ```python
    from django.contrib.auth.models import User
    
    # Create a new user
    user = User.objects.create_user('john', 'john@example.com', 'password123')
    
    # Retrieve a user based on username
    user = User.objects.get(username='john')
    
    ```
2. **Authentication Middleware**

    Django incorporates authentication middleware that `seamlessly associates users` with `incoming requests and grants access` to the authenticated user within `views and templates.`

3. **Authentication Backends**

    Authentication backends handle the process of `verifying user credentials`. Django provides several built-in authentication backends, with the most common being `ModelBackend` for authentication against the default User model.

## User Registration
User registration is the process of creating new user accounts in your application. Django provides the `UserCreationFormform` and the     `CreateView ` class-based view to handle user registration.

```python
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

```
In summary, for User Registrattin we need:
- A Django class called UserCreationForm for creating new user, including username and passowrd
- Create view class for handling the logic of the form submitted by tje users and submitting it to database


In this example, the `SignUpView` uses the `UserCreationForm` to handle user registration. When a new user is registered, they are redirected to the login page using the `success_url` attribute.