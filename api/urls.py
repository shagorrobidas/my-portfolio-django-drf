from django.urls import path, include

urlpatterns = [
    path(
        'main/',
        include('main.api.urls'),
        name='main'
    ),
    path(
        'resume/',
        include('resume.api.urls'),
        name='resume'
    ),
    path(
        'project/',
        include('project.api.urls'),
        name='project'
    ),
    path(
        'blog/',
        include('blog.api.urls'),
        name='blog'
    ),
    
]   