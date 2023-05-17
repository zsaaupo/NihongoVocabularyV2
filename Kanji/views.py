from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
import random

def Kanji(request):
    
    return render(request, 'Vocabulary.html')

        
class Kanji5(ListAPIView):
    serializer_class = KanjiN5Serializer
  
    def get_queryset(self):
        data_list = list(KanjiN5.objects.all())
        random_data = random.sample(data_list, len(data_list))
        return random_data
    

class Kanji4(ListAPIView):
    serializer_class = KanjiN4Serializer
  
    def get_queryset(self):
        data_list = list(KanjiN4.objects.all())
        random_data = random.sample(data_list, len(data_list))
        return random_data