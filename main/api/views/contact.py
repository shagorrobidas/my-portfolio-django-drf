from rest_framework import generics
from main.models import ContactMessage
from main.api.serializers import ContactMessageSerializer


class ContactMessageCreate(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

