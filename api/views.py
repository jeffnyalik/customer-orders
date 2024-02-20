from rest_framework import viewsets
from api.models import Customer, Order
from serializers.customers.customers import CustomerSerializer
from serializers.orders.orders import OrderSerializer
import africastalking
from django.conf import settings


class CustomersViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrdersViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        customer = order.customer
        message = f"New order placed by {customer.name} for {order.item} successfully."
        send_sms_alert(customer.phone_number, message)


"""Send SMS Alert function"""
def send_sms_alert(phone_number, message):
    africastalking.initialize(
        username=settings.AFRICASTALKING_USERNAME,
        api_key=settings.AFRICASTALKING_API_KEY
    )

    sms = africastalking.SMS
    response = sms.send(message, [phone_number], settings.SENDER_SHORT_CODE)
    return response


