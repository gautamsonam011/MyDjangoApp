from django.db import models
from django.utils import timezone

# Create your models here.

class Member(models.Model):
    firstName = models.CharField(max_length=240)
    lastName = models.CharField(max_length=240)
    age = models.CharField(max_length=240)
    mobile = models.CharField(max_length=12)
    joined_date = models.DateField(default="12/12/2024")  