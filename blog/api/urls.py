from django.urls import path, include
from blog.api.views import PostViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'blog-categories', CategoryViewSet, basename='blog-categories')

urlpatterns = [
    path(
        '',
        include(router.urls)
    ),
]