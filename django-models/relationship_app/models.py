from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
##author: This is another attribute (field) of the Book model that represents a relationship between the Book model and the Author model.
## ForeignKey: This is a field type in Django that creates a many-to-one relationship with another model. In this context, it means that each Book is associated with one Author, but each Author can be associated with multiple books.
    def __str__(self) -> str:
         return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    def __str__(self) -> str:
        return self.title
    
class Library(models.Model):
     name = models.CharField(max_length=100)
     books = models.ManyToManyField(Book,related_name='libraries')

     def __str__(self) -> str:
         return self.name
class Librarian(models.Model):
      name = models.CharField(max_length=100)
      library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='liberian')
      def __str__(self) -> str:
         return self.name