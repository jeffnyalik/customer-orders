from django.urls import include, path
from rest_framework import routers
from api.views import CustomersViewSets, OrdersViewSets
from .sms_callback_view import SMSCallbackView

router = routers.DefaultRouter()
router.register(r'customers', CustomersViewSets, basename='customers')
router.register(r'orders', OrdersViewSets, basename='orders')

urlpatterns = [
    path("", include(router.urls)),
    path('sms_callback/', SMSCallbackView.as_view(), name='sms_callback')
]