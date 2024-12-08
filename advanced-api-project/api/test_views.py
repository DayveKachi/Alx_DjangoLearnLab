from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import Book, Author
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class BookApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="123")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_create_book_authenticated(self):
        self.author = Author.objects.create(name="bruce wayne")
        url = reverse("book_create")
        data = {
            "title": "latest archie",
            "author": self.author.pk,
            "publication_year": 2023,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
