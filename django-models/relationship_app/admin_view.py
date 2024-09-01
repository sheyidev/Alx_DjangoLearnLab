# views/admin_view.py

from django.shortcuts import render
from django.http import HttpResponseForbidden
from decorators import admin_required

@admin_required
def admin_view(request):
    # Your view logic here
    return render(request, 'admin_dashboard.html')
