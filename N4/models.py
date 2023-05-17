from django.db import models
from N5.models import *

# N4 models with all abstract models inherited
class VocabularyListN4(VocabularyList):
    
    def __str__(self):
        return self.list_number


class VocabularyN4(Vocabulary):
    vocabulary_list = models.ForeignKey(VocabularyListN4, on_delete=models.PROTECT, related_name="vocabulary")
    
    def __str__(self):
        return self.nihongo + " " + self.english