from rest_framework import generics
from main.models import Profile
from main.api.serializers import ProfileSerializer

class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get_object(self):
        return Profile.objects.first()