from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from api.models import Customer


class OrderAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a Customer instance to associate with the order
        self.customer = Customer.objects.create(name='customerb', code='JF0001', phone_number='+254716431039')
        self.order_data = {'item': 'food', 'amount': '30.34', 'time': '2024-02-19T09:19:25', 'customer': self.customer.id}
    
    def test_create_orders(self):
        url = "/api/v1/orders/"
        response = self.client.post(url, self.order_data, format='json')

        # Assert status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)