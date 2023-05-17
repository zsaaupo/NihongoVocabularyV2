from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
import random


def N4(request):
    
    return render(request, 'Vocabulary.html')


class VocabularyListN4API(ListAPIView):
    serializer_class = VocabularyListN4Serializer

    def get_queryset(self):
        return VocabularyListN4.objects.all()
        
class VocabularyN4API(ListAPIView):
    serializer_class = VocabularyN4Serializer

    def get_queryset(self):
        list_number = self.kwargs['list_number']
        vocabulary_list = VocabularyListN4.objects.get(list_number=list_number)
        data_list = list(VocabularyN4.objects.filter(vocabulary_list=vocabulary_list))
        random_data = random.sample(data_list, len(data_list))
        return random_data