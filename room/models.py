from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    booked = models.BooleanField(max_length=200)
    
