# views/admin_view.py
from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib.auth.admin import UserAdmin


class CustomAdmin(UserAdmin):
    model = UserProfile
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("name")}),
    )
    admin.site.register(UserProfile)


def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


@user_passes_test(is_admin)
def admin_only_view(request):
    return HttpResponse("This view is for Admins only.")