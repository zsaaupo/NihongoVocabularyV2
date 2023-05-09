from rest_framework import serializers
from .models import *

class VocabularyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = VocabularyList
        fields = ["list_number"]
 

class VocabularySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vocabulary
        fields = "__all__"