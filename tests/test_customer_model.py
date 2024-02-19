from django.test import TestCase
from api.models import Customer
from django.utils import timezone

class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(name='John Doe', code='JD001')

    def test_name_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_code_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('code').verbose_name
        self.assertEquals(field_label, 'code')

    def test_name_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('name').max_length
        self.assertEquals(max_length, 250)

    def test_code_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('code').max_length
        self.assertEquals(max_length, 50)