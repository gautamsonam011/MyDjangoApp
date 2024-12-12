from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=240)
    lastName = models.CharField(max_length=240)
    age = models.CharField(max_length=240)
    mobile = models.CharField(max_length=12)
    joined = models.DateField(default=timezone.now)
    email = models.EmailField(max_length=240, null=True, blank=True)