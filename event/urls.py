
from django.urls import path, include
from event.views import *
from rest_framework import routers


urlpatterns = [
    
    path("bookings/", BookingApiView.as_view()),
    path("booking/cancel/<int:id>", CancelBooking.as_view()),
    path("create/", CreateEventApiView.as_view()),
    path("cancel/<int:id>", CancelEventApiView.as_view()),
    path("", EventApiView.as_view()),

]