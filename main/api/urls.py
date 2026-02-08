from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.api.views import (
    ProfileDetail,
    ServiceViewSet,
    TestimonialViewSet,
    ContactMessageCreate
)



router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'testimonials', TestimonialViewSet)
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
    path(
        'contact/',
        ContactMessageCreate.as_view(),
        name='contact'
    )
]