from rest_framework import serializers
from .models import *

class VocabularyListN5Serializer(serializers.ModelSerializer):

    class Meta:
        model = VocabularyListN5
        fields = ["list_number"]
 

class VocabularyN5Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = VocabularyN5
        fields = "__all__"