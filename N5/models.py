from django.db import models


class VocabularyList(models.Model):
    list_number = models.CharField(max_length=2)

    def __str__(self):
        return "List Number "+str(self.list_number)
    

class Vocabulary(models.Model):
    vocabulary_list = models.ForeignKey(VocabularyList, on_delete=models.PROTECT, related_name="vocabulary")
    english = models.CharField(max_length=100)
    nihongo = models.CharField(max_length=100)
    bangla = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nihongo + " " + self.english