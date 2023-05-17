from django.contrib import admin
from .models import *


class KanjiN5Admin(admin.ModelAdmin):
    
    fields = [
        "kanji",
        "nihongo"
    ]
    
admin.site.register(KanjiN5, KanjiN5Admin)


class KanjiN4Admin(admin.ModelAdmin):
    
    fields = [
        "kanji",
        "nihongo"
    ]
    
admin.site.register(KanjiN4, KanjiN4Admin)