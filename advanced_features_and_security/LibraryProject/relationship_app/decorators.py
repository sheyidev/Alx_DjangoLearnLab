# decorators.py

from django.contrib.auth.decorators import user_passes_test

def admin_required(function=None):
    """
    Decorator for views that checks whether a user is in the 'Admin' group,
    redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.groups.filter(name='Admin').exists(),
        login_url='/login/',  # Redirect to your login page
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
