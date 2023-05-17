from django.contrib import admin
from .models import *


class VocabularyListN4Admin(admin.ModelAdmin):
    
    fields = [
        "list_number"
    ]
    
admin.site.register(VocabularyListN4, VocabularyListN4Admin)


class VocabularyN4Admin(admin.ModelAdmin):
    
    fields = [
        "vocabulary_list",
        "nihongo",
        "english",
        "bangla"
    ]
    
admin.site.register(VocabularyN4, VocabularyN4Admin)