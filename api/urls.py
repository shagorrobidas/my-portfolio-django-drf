from django.urls import path, include

urlpatterns = [
    path('', include('main.api.urls')),
    path('', include('resume.api.urls')),
    path('', include('project.api.urls')),
    path('', include('blog.api.urls')),
]