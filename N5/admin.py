from django.contrib import admin
from .models import *




class VocabularyListAdmin(admin.ModelAdmin):
    
    fields = [
        "list_number"
    ]
    
admin.site.register(VocabularyList, VocabularyListAdmin)


class VocabularyAdmin(admin.ModelAdmin):
    
    fields = [
        "vocabulary_list",
        "nihongo",
        "english",
        "bangla"
    ]
    
admin.site.register(Vocabulary, VocabularyAdmin)