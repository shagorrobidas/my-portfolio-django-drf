from rest_framework import viewsets
from blog.models import Category
from blog.api.serializers.category_serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
