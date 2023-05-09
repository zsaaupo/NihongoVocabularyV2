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