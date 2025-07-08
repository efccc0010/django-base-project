from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Book


class BookModelTest(TestCase):
    def test_create_book(self):
        book = Book.objects.create(
            title="Clean Code", author="Robert C. Martin", published="2008-08-01"
        )
        self.assertEqual(book.title, "Clean Code")
        self.assertEqual(str(book), "Clean Code")


class AuthTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_jwt_login(self):
        response = self.client.post(
            "/api/token/", {"username": "testuser", "password": "testpass"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)  # type: ignore
