from rest_framework import serializers
from main.models import Profile, ProfileSection


class ProfileSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSection
        fields = ['id', 'title', 'content', 'order']


class ProfileSerializer(serializers.ModelSerializer):
    linkedin = serializers.CharField(source='linkedin_username', read_only=True)
    github = serializers.CharField(source='github_username', read_only=True)
    sections = ProfileSectionSerializer(many=True, read_only=True)
    titles = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id',
            'name',
            'title',
            'titles',
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
            'about_text_extra',
            'sections'
        ]
        read_only_fields = ('id',)

    def get_titles(self, obj):
        dynamic_titles = list(obj.titles.all().values_list('title', flat=True))
        if dynamic_titles:
            return dynamic_titles
        if obj.title:
            return [t.strip() for t in obj.title.split(',') if t.strip()]
        return []
