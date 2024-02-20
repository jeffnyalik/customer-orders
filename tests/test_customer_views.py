from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from oauth2_provider.models import AccessToken

from authentication.models import CustomUser


class CustomerAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer_data = {'name': 'customera', 'code': 'code2030', 'phone_number': '+254716431039'}

        # Create a user and obtain a token for authentication
        self.user = CustomUser.objects.create_user(email='testuser@gmail.com', password='password')

        self.access_token = AccessToken.objects.create(
            user=self.user,
            token='my-access-token',
            expires='2024-12-31 23:59:59',
            scope='read write',
        )
    
    def test_create_customers(self):
        url = "/api/v1/customers/"
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token.token)
        response = self.client.post(url, self.customer_data)

        # Assert status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)