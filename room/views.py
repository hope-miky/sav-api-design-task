from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from room.serializeres import RoomSerializer
from room.models import Room
# Create your views here.


class RoomApiView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # pagination_class = StandardAppPagination
