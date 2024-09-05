from django.contrib import admin
from .models import Book, CustomUser, CustomerUserAdmin
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year')
    admin.site.register(CustomUser, CustomerUserAdmin)