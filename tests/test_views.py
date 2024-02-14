from rest_framework.test import APIClient
from django.test import TestCase
from snipptes.models import Snippets
from django.urls import reverse
from rest_framework import status

class SnippetsApiViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.snippet_data = {'name': 'Test Snippet', 'code': 'print("Hello, world!")'}

    def test_get_snippets(self):
        # Create some snippets
        snippet1 = Snippets.objects.create(name='Snippet 1', code='print("Snippet 1")')
        snippet2 = Snippets.objects.create(name='Snippet 2', code='print("Snippet 2")')

        # Make GET request to the view
        response = self.client.get(reverse('Snippets-list'))

        # Assert status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert response data
        self.assertEqual(len(response.data), 2)  # Assuming there are only 2 snippets in the database

    def test_create_snippet(self):
        # Make POST request to the view
        response = self.client.post(reverse('Snippets-list'), self.snippet_data)

        # Assert status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_update_Snippets(self):
    #     # Create a Snippets
    #     snippets = Snippets.objects.create(name='Original Snippets', code='print("Original Snippets")')
    #     new_data = {'name': 'Updated Snippets', 'code': 'print("Updated Snippets")'}

    #     # Make PUT request to update the Snippets
    #     response = self.client.put(reverse('Snippetss-detail', kwargs={'pk': snippets.pk}), new_data)

    #     # Assert status code
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Refresh the Snippets from the database
    #     Snippets.refresh_from_db()

    #     # Assert Snippets has been updated
    #     self.assertEqual(Snippets.name, 'Updated Snippets')

    # def test_delete_Snippets(self):
    #     # Create a Snippets
    #     Snippets = Snippets.objects.create(name='Snippets to Delete', code='print("Snippets to Delete")')

    #     # Make DELETE request to delete the Snippets
    #     response = self.client.delete(reverse('Snippetss-detail', kwargs={'pk': Snippets.pk}))

    #     # Assert status code
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     # Assert Snippets has been deleted
    #     self.assertFalse(Snippets.objects.filter(pk=Snippets.pk).exists())

    # def test_invalid_Snippets_data(self):
    #     # Make POST request with invalid data
    #     invalid_data = {'name': '', 'code': ''}
    #     response = self.client.post(reverse('Snippets-list'), invalid_data)

    #     # Assert status code
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    #     # Assert error messages
    #     self.assertIn('name', response.data)
    #     self.assertIn('code', response.data)

    # Add more tests as needed
