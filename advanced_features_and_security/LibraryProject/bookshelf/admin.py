from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
admin.site.register(CustomUser, CustomUserAdmin)




#     The `Book` model is registered with the Django admin interface by adding the following code to `admin.py`:

# ```python
# from django.contrib import admin
# from .models import Book

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'publication_year')
#     search_fields = ('title', 'author')
#     list_filter = ('publication_year',)
