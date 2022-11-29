from django.db import models
from django.contrib.auth.models import User
from room.models import Room
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()


class Booking(models.Model):
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    table_settings = models.CharField(max_length=200)
    date = models.DateTimeField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    number_of_people = models.IntegerField()