from rest_framework import serializers
from main.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    linkedin = serializers.CharField(source='linkedin_username', read_only=True)
    github = serializers.CharField(source='github_username', read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'name',
            'title',
            'avatar',
            'email',
            'linkedin',
            'github',
            'linkedin_username',
            'linkedin_url',
            'github_username',
            'github_url',
            'birthday',
            'location',
            'about_text',
            'about_text_extra'
        ]
        read_only_fields = ('id',)
