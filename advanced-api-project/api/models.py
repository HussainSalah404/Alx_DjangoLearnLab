from django.db import models

# The Author model represents a writer.
# Each Author can be linked to multiple books through the Book model.
class Author(models.Model):
    # Stores the full name of the author.
    name = models.CharField(max_length=100)

    def __str__(self):
        # String representation used in admin and shell for readability.
        return self.name


# The Book model represents a single book.
# Each book has one Author (many-to-one relationship).
class Book(models.Model):
    # Title of the book.
    title = models.CharField(max_length=200)

    # Publication year of the book (stored as integer for simplicity).
    publication_year = models.IntegerField()

    # ForeignKey creates a many-to-one relationship:
    # - Many books can belong to one Author.
    # - on_delete=models.CASCADE means if an Author is deleted,
    #   all their related Books are also deleted.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        # String representation of the Book (used in admin and shell).
        return self.title