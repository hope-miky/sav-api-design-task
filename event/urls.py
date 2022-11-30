
from django.urls import path, include
from event.views import *
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r"booking", BookingApiView)
router.register(r"", EventApiView)

urlpatterns = [
    path("", include(router.urls)),
]