from django.db import models
from django.contrib.auth.models import User
from room.models import Room
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200, help_text=("help text for name"),  )
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    from_date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    to_date = models.DateField()
    status = models.CharField(choices=[("Active", "active"), ("Canceled", "canceled")], max_length=50, default="active")

class Booking(models.Model):
    date = models.DateField()
    number_of_people = models.IntegerField()
    note = models.CharField(max_length=200)
    table_settings = models.CharField(max_length=200)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE)
    status = models.CharField(choices=[("Active", "active"), ("Canceled", "canceled")], max_length=50, default="active")