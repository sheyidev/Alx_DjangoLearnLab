from django.contrib import admin
from bookshelf.models import Book 
## Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("tittle", "author")
    pass
admin.site.register(Book)