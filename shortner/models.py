from django.db import models

# Create your models here.
# Data object which stores URL and shortened URl of the given URL 
class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)