from django.db import models

# Create your models here.

class Authors(models.Model):
   username = models.CharField(max_length=64,blank=False,unique=True)
   first_name = models.CharField(max_length=64,blank=False)
   last_name = models.CharField(max_length=64,blank=False)
   email = models.EmailField(max_length=70,blank=False)

