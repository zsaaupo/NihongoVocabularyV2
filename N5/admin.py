from django.contrib import admin
from .models import *


class VocabularyListN5Admin(admin.ModelAdmin):
    
    fields = [
        "list_number"
    ]
    
admin.site.register(VocabularyListN5, VocabularyListN5Admin)


class VocabularyN5Admin(admin.ModelAdmin):
    
    fields = [
        "vocabulary_list",
        "nihongo",
        "english",
        "bangla"
    ]
    
admin.site.register(VocabularyN5, VocabularyN5Admin)