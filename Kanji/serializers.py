from rest_framework import serializers
from .models import *
from N4.serializers import *
from N5.serializers import *

class KanjiN5Serializer(serializers.ModelSerializer):

    nihongo = VocabularyN5Serializer(many=False)
    class Meta:
        model = KanjiN5
        fields = "__all__"
 

class KanjiN4Serializer(serializers.ModelSerializer):
    
    nihongo = VocabularyN4Serializer(many=False)
    class Meta:
        model = KanjiN4
        fields = "__all__"