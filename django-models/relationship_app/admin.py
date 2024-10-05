from django.contrib import admin
from .models import Author
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = ("title", "author", "publication_year")
    search_fields = ("tittle", "author")
    pass
admin.site.register(Author)