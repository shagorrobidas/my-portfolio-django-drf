from django.urls import path, include
from rest_framework.routers import DefaultRouter
from resume.api.views import ExperienceViewSet, EducationViewSet, SkillViewSet

router = DefaultRouter()
router.register(r'experience', ExperienceViewSet)
router.register(r'education', EducationViewSet)
router.register(r'skills', SkillViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
