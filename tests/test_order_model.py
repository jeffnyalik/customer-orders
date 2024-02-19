from django.test import TestCase
from api.models import Customer,Order
from django.utils import timezone

class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        customer = Customer.objects.create(name='John Doe', code='JD001')
        Order.objects.create(customer=customer, item='Food', amount=30.34, time=timezone.now())

    def test_customer_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('customer').verbose_name
        self.assertEquals(field_label, 'customer')

    def test_item_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('item').verbose_name
        self.assertEquals(field_label, 'item')

    def test_amount_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('amount').verbose_name
        self.assertEquals(field_label, 'amount')

    def test_time_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('time').verbose_name
        self.assertEquals(field_label, 'time')

    def test_amount_max_digits(self):
        order = Order.objects.get(id=1)
        max_digits = order._meta.get_field('amount').max_digits
        self.assertEquals(max_digits, 10)

    def test_amount_decimal_places(self):
        order = Order.objects.get(id=1)
        decimal_places = order._meta.get_field('amount').decimal_places
        self.assertEquals(decimal_places, 2)