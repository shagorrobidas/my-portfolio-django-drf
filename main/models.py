from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Your Name")
    title = models.CharField(max_length=100, default="Python Backend Developer")
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField(default="you@email.com")
    linkedin_username = models.CharField(max_length=100, default="@yourhandle")
    linkedin_url = models.URLField(default="https://linkedin.com/in/yourhandle")
    github_username = models.CharField(max_length=100, default="@yourgithub")
    github_url = models.URLField(default="https://github.com/yourgithub")
    birthday = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, default="Your City, Country")
    about_text = models.TextField(blank=True)
    about_text_extra = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon_svg = models.TextField(help_text="Paste SVG path or full SVG here")

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_initials = models.CharField(max_length=5)
    text = models.TextField()

    def __str__(self):
        return self.client_name
    

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name}"
    
    class Meta:
        ordering = ['-created_at']