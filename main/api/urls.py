from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.api.views import (
    ProfileDetail,
    ServiceViewSet,
    TestimonialViewSet,
    ContactMessageCreate,
    ClientViewSet,
    SocialLinkViewSet
)

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'social-links', SocialLinkViewSet)
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