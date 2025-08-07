from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author  # Adjust import if needed
from django.urls import reverse
from rest_framework.authtoken.models import Token


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


        # Create an author and some books
        self.author = Author.objects.create(name="Chinua Achebe")
        self.book1 = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=self.author)
        self.book2 = Book.objects.create(title="No Longer at Ease", publication_year=1960, author=self.author)

        
    def test_create_book(self):
        print("Before create:", Book.objects.count())

        url = '/api/books/'  # Assuming this is your create/list endpoint
        data = {
            "title": "Things Fall Apart",
            "publication_year": 1958,
            "author": self.author.id
        }

        before_count = Book.objects.count()
        print("Before create:", before_count)

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("title", response.data)
        self.assertEqual(response.data["title"], "Things Fall Apart")
        self.assertEqual(Book.objects.count(),before_count + 1)
        self.assertEqual(Book.objects.last().title, "Things Fall Apart")

    def test_example(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIsInstance(response.data, list)
        self.assertGreater(len(response.data), 0)
        self.assertIn("title", response.data[0])