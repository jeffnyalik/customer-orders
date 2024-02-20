from rest_framework.views import APIView
from rest_framework.response import Response
from .views import send_sms_alert
import json


class SMSCallbackView(APIView):
    def post(self, request, format=None):
        # Extract necessary information from the callback
        callback_data = json.loads(request.body)
        message = callback_data['SMSMessageData']['Message']
        recipients = callback_data['SMSMessageData']['Recipients']
        
        # Process the callback data and perform any necessary actions for each recipient
        for recipient in recipients:
            status_code = recipient['statusCode']
            phone_number = recipient['number']
            status = recipient['status']
            cost = recipient['cost']
            message_id = recipient['messageId']
            
            # Perform actions based on the recipient's status code and other information
            if status_code == 101:  # Successful delivery
                # Example: Update the order status based on the successful delivery
                # order = Order.objects.get(phone_number=phone_number)
                # order.status = 'Delivered'
                # order.save()
                
                # Example: Send a response SMS to the customer
                response_message = f"Your order has been delivered. Thank you!"
                send_sms_alert(phone_number, response_message)
            
            # You can add more conditions based on different status codes if needed
            
        # Example: Print the received data
        print(f"Received SMS callback - Message: {message}")
        print(f"Received SMS callback - Recipients: {recipients}")

        # Example: Send a response
        return Response(status=200)