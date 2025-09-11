from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class Book(models.Model):
    """
    Represents a book in the system.

    Attributes:
        title (str): The title of the book. 
                        Limited to 200 characters.
        author (str): The author of the book. 
                        Limited to 100 characters.
        published_date (int): The year the book was published.
                                Stored as an integer.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.published_date})"

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field is required")
        if not extra_fields.get("date_of_birth"):
            raise ValueError("The date_of_birth field is required")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)

    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
    
class CustomPermissions(models.Model):  
    name = models.CharField(max_length=100)
    class Meta:
        permissions = [
                ("can_view", "Can view"),
                ("can_create", "Can create"),
                ("can_edit", "Can edit"),
                ("can_delete", "Can Delete")
            ]
