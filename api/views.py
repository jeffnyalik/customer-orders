from rest_framework import viewsets
from api.models import Customer, Order
from serializers.customers.customers import CustomerSerializer
from serializers.orders.orders import OrderSerializer

class CustomersViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrdersViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
