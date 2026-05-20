from project.models import Project
from main.models import ContactMessage
from blog.models import Post
from resume.models import Skill
from job_manager.models import JobApplication

def dashboard_callback(request, context):
    context.update({
        "custom_kpi": [
            {
                "title": "Total Projects",
                "metric": Project.objects.count(),
                "footer": "Portfolio projects",
                "icon": "business_center"
            },
            {
                "title": "Total Messages",
                "metric": ContactMessage.objects.count(),
                "footer": "From contact form",
                "icon": "mail"
            },
            {
                "title": "Blog Posts",
                "metric": Post.objects.count(),
                "footer": "Published articles",
                "icon": "article"
            },
            {
                "title": "Skills Listed",
                "metric": Skill.objects.count(),
                "footer": "In resume section",
                "icon": "psychology"
            },
            {
                "title": "AI Jobs Applied",
                "metric": JobApplication.objects.count(),
                "footer": "OpenAI Applications",
                "icon": "smart_toy"
            },
        ],
    })
    return context
