from rest_framework import viewsets
from blog.models import Post
from blog.api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer