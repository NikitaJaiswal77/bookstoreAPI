from rest_framework.test import APITestCase
from rest_framework import status
from myapp.models import Book

class BookTests(APITestCase):
    def test_create_book(self):
        url = '/api/books/'  
        data = {
            'title': 'New Book',
            'author': 'Author Name',
            'publication_date': '2023-12-01',
            'isbn': '1234567890123',
            'price': 19.99,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  

    def test_get_books(self):
        url = '/api/books/'  
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
