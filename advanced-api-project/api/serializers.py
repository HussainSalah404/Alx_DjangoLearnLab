from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# Serializer for the Book model.
# Converts Book objects to JSON and validates input data before saving.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # "__all__" means all fields of the Book model will be serialized
        # (id, title, published_date, author).
        fields = "__all__"

    # Custom field-level validation for "published_date".
    # Ensures the publication year is not set in the future.
    def validate_published_date(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# Serializer for the Author model.
# Includes the Author’s name and all related books (nested serialization).
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to display books for each author.
    # - "many=True" because an author can have multiple books.
    # - "read_only=True" so books cannot be created/edited via AuthorSerializer.
    # - "source='book_set'" tells DRF to use the reverse relationship
    #    automatically created by Django (author.book_set).
    books = BookSerializer(many=True, read_only=True)
    

    class Meta:
        model = Author
        # Only expose the name and the nested list of books.
        fields = ["name", "books"]