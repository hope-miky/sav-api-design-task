from rest_framework import serializers
from event.models import  Event, Booking

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        # exclude = ('owner',)

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        # exclude = ('owner',)
        