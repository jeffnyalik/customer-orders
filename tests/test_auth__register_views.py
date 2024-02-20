from rest_framework.test import APITestCase
from authentication.models import CustomUser
from rest_framework import status

class UserRegistrationAPIViewTest(APITestCase):
    def test_user_registration(self):
        url = '/authentication/register'  # Assuming you have defined the URL name for UserRegistrationAPIView
        data = {
            'email': 'testuser@gmail.com',
            'password': 'testpassword',
            # Include other required fields for user registration
        }
        response = self.client.post(url, data)

        # Assert the response status code and any other assertions based on your expected behavior
        self.assertEqual(response.status_code, 201)  # Assuming you expect a 201 Created status code
        # Add additional assertions if needed
