The error message indicates that Django tried to access a `Library` object with a primary key (`pk`) of `1` but couldn't find a matching object in the database. 

### Possible Causes and Solutions

1. **No `Library` Object with the Given Primary Key**:
   The primary key (`pk=1`) you are trying to access does not exist in your `Library` model's table.

2. **Incorrect Primary Key**:
   If you meant to access a different library object, you need to use the correct primary key.

### Steps to Resolve the Issue

#### 1. **Check if a `Library` Object Exists**

To verify whether a `Library` object with a primary key of `1` exists, you can use the Django shell.

- **Open the Django Shell**:

  ```bash
  python manage.py shell
  ```

- **Check for Library Objects**:

  ```python
  from relationship_app.models import Library

  # Check if any Library object exists
  libraries = Library.objects.all()
  print(libraries)
  ```

  If `libraries` is an empty query set (`<QuerySet []>`), it means there are no `Library` objects in the database.

#### 2. **Create a `Library` Object If None Exists**

If no `Library` object exists or if you want to ensure there’s an object with a specific primary key, create one:

- **In the Django Shell**:

  ```python
  from relationship_app.models import Library

  # Create a new Library object
  library = Library.objects.create(name="Central Library")
  print(library.pk)  # This will print the primary key of the created Library object
  ```

- After creating the `Library` object, note the primary key printed. Use this primary key in your URL.

#### 3. **Access the Correct URL with Existing Primary Key**

Now, update the URL in your browser to use the correct primary key:

```
http://127.0.0.1:8000/relationship_app/library/<pk>/
```

Replace `<pk>` with the primary key of the `Library` object you just created or verified in the shell.

#### 4. **Recheck the URL Configuration**

Ensure that your `urls.py` is correctly configured to use the primary key:

```python
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name="library_view"),
]
```

### Summary

- **Check if `Library` objects exist** using the Django shell.
- **Create a `Library` object** if none exists.
- **Access the detail view with the correct primary key** in the URL.
- **Ensure URL patterns are correct** and align with your view requirements.

By following these steps, you should be able to access the `LibraryDetailView` without encountering a 404 error.