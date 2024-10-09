from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
         permissions = [
                 ("can_add_book", "Can add book"),
                ("can_change_book", "Can change book"),
                ("can_delete_book", "Can delete book"),
              ]
    
    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')
    
    def __str__(self):
        return self.name
    

class Librarian(models.Model):
     name = models.CharField(max_length=200)
     library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')




class CustomUserManager(BaseUserManager):
    """custom manager for CustomUser with no username field"""
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")
        

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Encrypt the password
        user.save(using=self._db)  # Save to the database
        return user
    

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(username, email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
        # Use the custom user manager
    objects = CustomUserManager()

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    ROLES_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Role field with predefined choices
    role = models.CharField(max_length=10, choices=ROLES_CHOICES)
    
    def __str__(self):
        return f'{self.user} - {self.role}'
    
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
       if created:
           UserProfile.objects.create(user=instance)
       #instance.userprofile.save()



"""     # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Avoids the clash with default 'User.groups'
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Avoids the clash with default 'User.user_permissions'
        blank=True,
    )
    
    
    
    def __str__(self):
        return self.username
"""
 