from rest_framework import viewsets
from job_manager.models import JobApplication
from job_manager.api.serializers import JobApplicationSerializer

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all().order_by('-created_at')
    serializer_class = JobApplicationSerializer
