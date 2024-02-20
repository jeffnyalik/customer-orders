from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from api.models import Customer
from oauth2_provider.models import AccessToken
from authentication.models import CustomUser



class OrderAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a Customer instance to associate with the order
        self.customer = Customer.objects.create(name='customerb', code='JF0001', phone_number='+254716431039')
        self.order_data = {'item': 'food', 'amount': '30.34', 'time': '2024-02-19T09:19:25', 'customer': self.customer.id}

        # Create a user and obtain a token for authentication
        self.user = CustomUser.objects.create_user(email='test2user@gmail.com', password='password')
         # Create a user and obtain a token for authentication
        self.user = CustomUser.objects.create_user(email='testuser@gmail.com', password='password')

        self.access_token = AccessToken.objects.create(
            user=self.user,
            token='my-access-token',
            expires='2024-12-31 23:59:59',
            scope='read write',
        )

    
    def test_create_orders(self):
        url = "/api/v1/orders/"

        # Set the authentication header with the token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token.token)
        response = self.client.post(url, self.order_data, format='json')

        # Assert status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)