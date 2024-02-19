from django.http import HttpResponse
from rest_framework.views import APIView
from snipptes.models import *
from serializers.snippets.snippets import SnippetSerializers
from rest_framework.response import Response
from rest_framework import status


def index(request):
    # Initialize SDK
    username = "sandbox"    # use 'sandbox' for development in the test environment
    api_key = "f2e9836cb290ba3597e5addeca1e7081d3b10e093f54599950bbb885426fa898"      # use your sandbox app API key for development in the test environment
    africastalking.initialize(username, api_key)


    # Initialize a service e.g. SMS
    sms = africastalking.SMS
    # Use the service synchronously
    response = sms.send("Hello Message!", ["+254716431039"])
    print(response)
    return response



class SnippetsApiViews(APIView):
    def get(self, request, format=None):
        snippets = Snippets.objects.all()
        serializer = SnippetSerializers(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = SnippetSerializers(data=request.data)
        if(serializer.is_valid()):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
