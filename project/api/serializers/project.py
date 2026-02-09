from rest_framework import serializers
from project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    categories_list = serializers.SerializerMethodField()
    tags_list = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'categories',
            'categories_list',
            'description',
            'image',
            'tags',
            'github_link',
            'live_link',
            'tags_list'
        ]

    def get_categories_list(self, obj):
        return [cat.name for cat in obj.categories.all()]

    def get_tags_list(self, obj):
        return obj.get_tags_list()