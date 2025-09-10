from django.db import models
from django.contrib.auth.models import AbstractUser

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
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to="", blank=True, null=True)

    
    
    def __str__(self):
        return self.username