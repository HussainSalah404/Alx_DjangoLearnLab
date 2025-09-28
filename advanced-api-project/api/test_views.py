from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create an Author instance to use in tests
        self.author = Author.objects.create(name="Author 1")

        # Create a Book linked to the author
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2020
        )

        # Create API client
        self.client = APIClient()

    def test_create_book(self):
        # Authenticate before making the request
        self.client.login(username="testuser", password="password123")

        url = reverse("book-create")
        data = {
            "title": "New Book",
            "author": self.author.id,   # must be ID
            "publication_year": 2021
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")
        self.assertEqual(response.data["author"], self.author.id)

    def test_update_book(self):
        self.client.login(username="testuser", password="password123")

        url = reverse("book-update")
        data = {
            "id": self.book.id,
            "title": "Updated Title",
            "author": self.author.id,
            "publication_year": 2020
        }
        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_book(self):
        self.client.login(username="testuser", password="password123")

        url = reverse("book-delete")
        data = {"id": self.book.id}
        response = self.client.delete(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_read_books(self):
        # Reading does NOT require login
        url = reverse("book-list")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # at least one book
        self.assertEqual(response.data[0]["title"], "Test Book")