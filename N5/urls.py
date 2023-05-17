from django.urls import path
from .views import *

urlpatterns = [
    path('', N5),
    path('list/', VocabularyListN5API.as_view()),
    path('list/<str:list_number>', VocabularyN5API.as_view()),
]