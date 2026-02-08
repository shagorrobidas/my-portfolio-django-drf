from rest_framework import viewsets
from resume.models import Skill
from resume.api.serializers import SkillSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer