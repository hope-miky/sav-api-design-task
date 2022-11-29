from rest_framework.viewsets import ModelViewSet
from event.serializeres import EventSerializer
from event.models import Event

class EventApiView(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # pagination_class = StandardAppPagination