from rest_framework import serializers
from .models import *

class KanjiN5Serializer(serializers.ModelSerializer):

    class Meta:
        model = KanjiN5
        fields = "__all__"
 

class KanjiN4Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = KanjiN4
        fields = "__all__"