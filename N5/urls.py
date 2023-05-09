from django.urls import path
from .views import *

urlpatterns = [
    path('', N5),
    path('list/', VocabularyListAPI.as_view()),
]