from snipptes.models import *
from rest_framework import serializers

class SnippetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ['id', 'name']
        