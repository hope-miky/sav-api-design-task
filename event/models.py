from django.db import models
from django.contrib.auth.models import User
from room.models import Room
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    from_date = models.DateTimeField(max_length=200)
    to_date = models.DateTimeField(max_length=200)