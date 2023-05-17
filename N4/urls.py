from django.urls import path
from .views import *

urlpatterns = [
    path('', N4),
    path('list/', VocabularyListN4API.as_view()),
    path('list/<str:list_number>', VocabularyN4API.as_view()),
]