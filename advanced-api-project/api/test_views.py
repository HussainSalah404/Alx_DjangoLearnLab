from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a test user and log in
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")

        # Create a sample book
        self.book = Book.objects.create(title="Test Book", author="Author 1", publication_year=2020)

    def test_create_book(self):
        url = reverse("book-create")
        data = {"title": "New Book", "author": "Author 2", "publication_year": 2021}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        url = reverse("book-update")
        data = {"id": self.book.id, "title": "Updated Title", "author": "Author 1", "publication_year": 2020}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse("book-delete")
        data = {"id": self.book.id}
        response = self.client.delete(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_read_books(self):
        url = reverse("book-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)