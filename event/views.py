from typing import Any
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from event.serializeres import EventSerializer, BookingSerializer, EventModelSerializer, PlaceHolderSerializer
from event.models import Event, Booking
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, mixins, views, viewsets
from room.models import Room
from datetime import datetime
from datetime import timedelta
import traceback



class BookingApiView(generics.GenericAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        try:
            bookings = Booking.objects.filter().values()
            return Response({ "data": bookings }, status=status.HTTP_200_OK)

        except BaseException as e:
            print("")

    def delete(self, request):
        bookings = Booking.objects.filter()
        for booking in bookings:
            booking.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)



class EventApiView(generics.GenericAPIView):

    queryset = Event.objects.all()
    serializer_class = PlaceHolderSerializer

    def get(self, request):
        try:
            events = Event.objects.filter().values()
            return Response({ "data": events }, status=status.HTTP_200_OK)

        except BaseException as e:
            print(traceback.format_exc())
            return Response({ "error": f"{e}" }, status=status.HTTP_400_BAD_REQUEST)



class CancelEventApiView(generics.GenericAPIView):

    queryset = Event.objects.all()
    serializer_class = PlaceHolderSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def put(self, request, id):
        try:
            event = Event.objects.get(id=id)
            
            for booking in event.booking_set.filter():
                booking.status = "canceled"
                booking.save()
                print(f"booking {booking.date} canceled")

            return Response({ "status": f"Event {event.name} canceled " }, status=status.HTTP_200_OK)

        except BaseException as e:
            print("")
            return Response({ "error": f"{e}" }, status=status.HTTP_400_BAD_REQUEST)



class CreateEventApiView(generics.GenericAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]


    def check_room(self, request, serializer: int):

        room = Room.objects.get(id=serializer["room"])
        bookings = room.booking_set.filter(date__range=[serializer["from_date"], serializer["to_date"]])

        if bookings.count() > 0:
            raise ValueError(f"The room is already book for the following dates {bookings.values('date')}")

        date_from = datetime.strptime(serializer["from_date"], '%Y-%m-%d')
        date_to = datetime.strptime(serializer["to_date"], '%Y-%m-%d')

        event = Event(
            name = serializer["name"],
            description = serializer["description"],
            owner = request.user,
            from_date = date_from,
            from_time = serializer["from_time"],
            to_time = serializer["to_time"],
            to_date = date_to,
            status = "active",
        )
        try:
            event.save()
            while date_from != date_to:
                booking = Booking(
                    date = date_from,
                    number_of_people = serializer["num_peoples"],
                    note = serializer["note"],
                    table_settings = serializer["table_settings"],
                    room = room,
                    event = event,
                    status = "active",
                )
                booking.save()
                day_to_add = timedelta(days=1)
                date_from += day_to_add
                print(f"----- --------- created{booking}")
        except:
            event.delete()
            # print(traceback.format_exc())


        # while date_from == date_to:


    def post(self, request, *args, **kwargs):

        try:
            request_data = request.data
            request_data['owner'] = request.user.id
            serializer = self.get_serializer(data=request_data)
            serializer.is_valid(raise_exception=True)
            self.check_room(request, serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except BaseException as e:
            print("----------------*-----------------------")
            return Response({"error": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

class CancelBooking(generics.GenericAPIView):
    
    serializer_class = PlaceHolderSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def put(self, request, id):
        try:

            booking = Booking.objects.get(id=id)

            if booking.event.owner.id != request.user.id:
                raise ValueError("Yous are not allowed to cancel the event!")

            booking.status = 'canceled'
            booking.save()

            return Response({ "status": f"Booking canceled for {booking.date}" }, status=status.HTTP_200_OK)

        except BaseException as e:
            print("")
            return Response({"error": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)