from rest_framework import viewsets
from resume.models import Education
from resume.api.serializers import EducationSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer