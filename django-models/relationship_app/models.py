from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
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


class UserProfile(models.Model):
    ROLES_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Role field with predefined choices
    role = models.CharField(max_length=10, choices=ROLES_CHOICES)
    
    def __str__(self):
        return f'{self.user} - {self.role}'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
       if created:
           UserProfile.objects.create(user=instance)
       instance.userprofile.save()

