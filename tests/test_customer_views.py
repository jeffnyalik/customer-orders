from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status

class CustomerAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer_data = {'name': 'customera', 'code': 'code2030'}
    
    def test_create_customers(self):
        url = "/api/v1/customers/"
        response = self.client.post(url, self.customer_data)

        # Assert status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)