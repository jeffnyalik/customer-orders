from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import authenticate
from serializers.auth.auths import UserRegistrationSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
import requests
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class =  UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class LoginApiView(APIView):
    permission_classes = [permissions.AllowAny]
    @csrf_exempt
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
    
        if user is not None and user.check_password(password):
            login(request, user)
            
            """
            clientid=zAEdINoYPECSC1YaXZ4IWEGUbOGKs2SPPR209Inz
            client_secret=VkLuhS4WYQip7gaDWvbOR54kl5uOXwJO8d5PtFzSB0Us2VE7KOc0zinZ2KSGYutYKnT3PPpAHhJxD5tHcPB4Btpr7Kz1x93RjXP5oIXOIqDgQLnkkdbqlZXlSrFhRj7P
            """
            # Obtain access token
            token_endpoint = 'http://localhost:8000/o/token/'
            client_id = 'zAEdINoYPECSC1YaXZ4IWEGUbOGKs2SPPR209Inz'
            client_secret = 'VkLuhS4WYQip7gaDWvbOR54kl5uOXwJO8d5PtFzSB0Us2VE7KOc0zinZ2KSGYutYKnT3PPpAHhJxD5tHcPB4Btpr7Kz1x93RjXP5oIXOIqDgQLnkkdbqlZXlSrFhRj7P'

           
            token_request_data = {
                'grant_type': 'password',
                'username': username,
                'password': password,
                'client_id': client_id,
                'client_secret': client_secret,
            }

            # Fetch access token using requests
            response = requests.post(token_endpoint, data=token_request_data)
            # return response(response.json())
        
            if response.status_code == 200:
                token_response = response.json()
                # access_token = token_response.get('access_token') ## Get specific access token if needs be
                return Response({'detail': 'Login successful.', 'access_token': token_response})
            else:
                return Response(response.json(), status=401)
                # return Response({'error': 'Failed to obtain access token.'}, status=401)
        else:
            return Response({'error': 'Invalid credentials.'}, status=401)