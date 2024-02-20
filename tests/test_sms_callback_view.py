from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class SMSCallbackViewTestCase(APITestCase):
    def test_sms_callback(self):
        # Prepare the data for the callback
        callback_data = {
            "SMSMessageData": {
                "Message": "Test message",
                "Recipients": [
                    {
                        "statusCode": 101,
                        "number": "+1234567890",
                        "status": "Success",
                        "cost": "0.50",
                        "messageId": "+1234567890"
                    }
                ]
            }
        }

        # Make a POST request to the sms_callback URL
        url = '/api/v1/sms_callback/'
        response = self.client.post(url, data=callback_data, format='json')

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add additional assertions based on your expected behavior