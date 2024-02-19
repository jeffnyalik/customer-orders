from django.urls import include, path
from rest_framework import routers
from api.views import CustomersViewSets, OrdersViewSets


router = routers.DefaultRouter()
router.register(r'customers', CustomersViewSets, basename='customers')
router.register(r'orders', OrdersViewSets, basename='orders')

urlpatterns = [
    path("", include(router.urls))
]