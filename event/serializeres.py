from rest_framework import serializers
from event.models import  Event, Booking

class EventSerializer(serializers.ModelSerializer):

    room = serializers.IntegerField()
    num_peoples = serializers.IntegerField()
    note = serializers.CharField()
    table_settings = serializers.CharField()
    status = serializers.CharField()

    class Meta:
        model = Event
        fields = "__all__"
        # exclude = ('owner',)


class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        # exclude = ('owner',)


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        # exclude = ('owner',)
    
class PlaceHolderSerializer(serializers.Serializer):
    ...