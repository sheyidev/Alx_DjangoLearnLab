from django.db import models
#from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, BaseUserManager
## resources used
##https://www.geeksforgeeks.org/how-to-use-user-model-in-django/
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
    class Meta:
         permissions = [
                 ("can_add_book", "Can add book"),
                ("can_change_book", "Can change book"),
                ("can_delete_book", "Can delete book"),
              ]
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
      
## create a UserModel and extend the a one-to-one relationhip with inbuilt User model
## You want to store additional data in UserProfile, hence using it wothout modyfing the User Model

class UserProfile(models.Model):
   ## define roles in a tuple,(is this immutable?)

   ROLES_CHOICES = [
       ('Admin', 'Admin'),
       ('Librarian', 'Librarian'),
       ('Member', 'Member'),
   ]
   ## create a user with ibe-to-one link with User Model
   user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Role field with predefined choices
   role = models.CharField(max_length=10, choices=ROLES_CHOICES)


   def __str__(self) -> str:
       return f"self.user.username - self.role"
   
   @receiver(post_save, sender=User)
   def create_profile(sender, instance, created, **kwargs):
       if created:
           UserProfile.objects.create(user=instance)
       instance.userprofile.save()

  # @receiver(post_save, sender=User)
  # def save_profile(sender, instance, **kwargs):
  #     instance.profile.save()
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class CustomerUser(AbstractUser):
    objects = CustomUserManager()