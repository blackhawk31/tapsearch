from django.db import models

# Create your models here.
class Index(models.Model):
    document_id = models.IntegerField()
    key = models.CharField(max_length=120, null=False, blank=False)
    frequency = models.IntegerField(null=False,blank=False)
