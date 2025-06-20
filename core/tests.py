from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def test_create_book(self):
        book = Book.objects.create(
            title="Clean Code",
            author="Robert C. Martin",
            published="2008-08-01"
        )
        self.assertEqual(book.title, "Clean Code")
        self.assertEqual(str(book), "Clean Code")
