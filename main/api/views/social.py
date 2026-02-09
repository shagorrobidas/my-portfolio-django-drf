from rest_framework import viewsets
from main.models import SocialLink
from main.api.serializers import SocialLinkSerializer

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
