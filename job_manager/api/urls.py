from django.urls import path, include
from rest_framework.routers import DefaultRouter
from job_manager.api.views import JobApplicationViewSet

router = DefaultRouter()
router.register(r'job-applications', JobApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
