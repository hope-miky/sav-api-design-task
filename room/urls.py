
from django.urls import path, include
from room.views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"", RoomApiView)

urlpatterns = [
    path("", include(router.urls)),
]