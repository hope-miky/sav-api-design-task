from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from room.serializeres import RoomSerializer
from room.models import Room
# Create your views here.
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class RoomApiView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    # pagination_class = StandardAppPagination
