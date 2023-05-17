from django.db import models
from N5.models import VocabularyN5
from N4.models import VocabularyN4

class KanjiN5(models.Model):
    
    nihongo = models.ForeignKey(VocabularyN5, on_delete=models.PROTECT, related_name="vocabulary")
    kanji = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.kanji + " --- " + str(self.nihongo)
    

class KanjiN4(models.Model):
    
    nihongo = models.ForeignKey(VocabularyN4, on_delete=models.PROTECT, related_name="vocabulary")
    kanji = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.kanji + " --- " + str(self.nihongo)
    