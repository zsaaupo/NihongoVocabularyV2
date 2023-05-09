from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *


def N5(request):
    
    return render(request, 'N5.html')


class VocabularyListAPI(ListAPIView):
    serializer_class = VocabularyListSerializer

    def get_queryset(self):
        return VocabularyList.objects.all()
    

class VocabularyAPI(ListAPIView):
    serializer_class = VocabularySerializer

    def get_queryset(self):
        list_number = self.kwargs['list_number']  # Extract the list_number from URL kwargs
        return Vocabulary.objects.filter(vocabulary_list=list_number)