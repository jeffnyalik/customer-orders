from django.urls import path
from .views import UserRegistrationAPIView, LoginApiView

urlpatterns = [
    path('register', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login', LoginApiView.as_view(), name='user-login')
]
