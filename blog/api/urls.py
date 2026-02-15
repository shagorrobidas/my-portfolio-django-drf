from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.api.views import PostViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'blog-categories', CategoryViewSet, basename='blog-categories')

urlpatterns = [
    path(
        '',
        include(router.urls)
    ),
]