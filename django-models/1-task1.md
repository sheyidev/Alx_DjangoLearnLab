##  Django Views and URL Configuration

**Objective:** Develop proficiency in creating both function-based and class-based views in Django, and configuring URL patterns to handle web requests effectively. 

This task will help you understand different ways to define views and manage URL routing in Django.

## Task Description:
In your existing Django project, enhance the `relationship_app` by adding new views that display information about books and libraries. 

Implement both function-based and class-based views to handle these displays and configure the URL patterns to route these views correctly.

## Steps:
1. Implement Function-based View:

    - Create a function-based view in `relationship_app/views.py` that lists all books stored in the database.
    - This view should render a simple text list of book titles and their authors.
2. Implement Class-based View:

   - Create a class-based view in `relationship_app/views.py` that displays details for a specific library, listing all books available in that library.
   - Utilize Django’s ListView or DetailView to structure this class-based view.
3. Configure URL Patterns:

   - Edit `relationship_app/urls.py` to include URL patterns that route to the newly created views. Make sure to link both the function-based and class-based views.
4. Create Templates (Optional for Display):

   - For a more structured output, using the code below as templates for each view to render the information in HTML format instead of plain text.


## Template for Listing Books (list_books.html):
This template will be used by the function-based view to display a list of all books.

```python
<!-- list_books.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>List of Books</title>
</head>
<body>
    <h1>Books Available:</h1>
    <ul>
        {% for book in books %}
        <li>{{ book.title }} by {{ book.author.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>

```
## Template for Displaying Library Details (library_detail.html):

This template will be used by the class-based view to show details of a specific library, including all books available in that library.

```python
<!-- library_detail.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Library Detail</title>
</head>
<body>
    <h1>Library: {{ library.name }}</h1>
    <h2>Books in Library:</h2>
    <ul>
        {% for book in library.books.all %}
        <li>{{ book.title }} by {{ book.author.name }} (Published {{ book.publication_year }})</li>
        {% endfor %}
    </ul>
</body>
</html>

```

## Repo:

- GitHub repository: Alx_DjangoLearnLab
- Directory: django-models