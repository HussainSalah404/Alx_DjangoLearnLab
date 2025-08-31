from django.db import models

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