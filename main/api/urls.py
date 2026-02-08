from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.api.views import ProfileDetail

router = DefaultRouter()

urlpatterns = [
    path(
        'profile/',
        ProfileDetail.as_view(),
        name='profile'
    ),
    path(
        '',
        include(router.urls)
    ),
]