from django.db import models


# abtract models
class VocabularyList(models.Model):
    list_number = models.CharField(max_length=2, unique=True)

    class Meta:
        abstract = True
    

class Vocabulary(models.Model):
    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)
    bangla = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        abstract = True
        

# N5 models
class VocabularyListN5(VocabularyList):
    
    def __str__(self):
        return self.list_number


class VocabularyN5(Vocabulary):
    vocabulary_list = models.ForeignKey(VocabularyListN5, on_delete=models.PROTECT, related_name="vocabulary")
    
    def __str__(self):
        return self.nihongo + " " + self.english