from django.http import HttpResponse
from rest_framework.views import APIView
from snipptes.models import *
from serializers.snippets.snippets import SnippetSerializers
from rest_framework.response import Response
from rest_framework import status

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
