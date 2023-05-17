from rest_framework import serializers
from .models import *

class VocabularyListN4Serializer(serializers.ModelSerializer):

    class Meta:
        model = VocabularyListN4
        fields = ["list_number"]
 

class VocabularyN4Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = VocabularyN4
        fields = "__all__"