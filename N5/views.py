from django.shortcuts import render
from .models import *


def N5(request):
    
    return render(request, 'N5.html')