from rest_framework import serializers
from project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    tags_list = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'category',
            'category_name',
            'description',
            'image',
            'tags',
            'github_url',
            'live_url',
            'tags_list'
        ]

    def get_tags_list(self, obj):
        return obj.get_tags_list()