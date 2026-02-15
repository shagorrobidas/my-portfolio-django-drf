from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    categories_list = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_categories_list(self, obj):
        return [c.name for c in obj.categories.all()]