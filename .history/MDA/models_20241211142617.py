from django.db import models

# Create your models here.

class Member(models.Model):
    firstName = models.CharField(max_length=240)
    lastName = models.CharField(max_length=240)
    age = models.CharField(max_length=240)
    mobile = models.CharField(max_length=12)
    
