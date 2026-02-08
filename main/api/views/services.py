from rest_framework import viewsets
from main.models import Service
from main.api.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer