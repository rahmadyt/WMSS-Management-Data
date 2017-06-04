from django.db import models

# Create your models here.

class Pencarian_Keyword(models.Model):
    url = models.CharField(max_length = 100)
    keyword = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.url