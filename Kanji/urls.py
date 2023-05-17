from django.urls import path
from .views import *

urlpatterns = [
    path('N5/', Kanji),
    path('N4/', Kanji),
    path('N5API/', Kanji5.as_view()),
    path('N4API/', Kanji4.as_view()),
]