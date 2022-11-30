from typing import Any
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from event.serializeres import EventSerializer, BookingSerializer
from event.models import Event, Booking
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, mixins, views
from room.models import Room
from datetime import datetime

class BookingApiView(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]


class EventApiView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                #    mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]


    def check_room(self, event: int):

        room = Room.objects.get(id=event["room"])
        bookings = room.booking_set.filter(date__range=[event["from_date"], event["to_date"]])

        if bookings.count() > 0:
            raise ValueError(f"The room is already book for the following dates {bookings.values('date')}")

        date_from = datetime.strptime(event["from_date"], '%Y-%m-%d')
        date_to = datetime.strptime(event["to_date"], '%Y-%m-%d')


        print(f"----------------{date_from}-----------{date_to}")
        # while date_from == date_to:


    def create(self, request, *args, **kwargs):

        request_data = request.data
        request_data['owner'] = request.user.id
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.check_room(serializer.data)
        # self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
