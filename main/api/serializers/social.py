from rest_framework import serializers
from main.models import SocialLink

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'
