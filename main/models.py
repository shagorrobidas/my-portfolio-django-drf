from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Your Name")
    title = models.CharField(
        max_length=300,
        default="Python Backend Developer",
        help_text="Comma-separated titles for typing rotation effect, e.g. Django Developer, Backend Engineer, Junior Software Engineer"
    )
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


class ProfileTitle(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='titles')
    title = models.CharField(max_length=150)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ProfileSection(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or self.content[:50]


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon_class = models.CharField(max_length=100, help_text="Font Awesome class, e.g. fa-solid fa-code", default="fa-solid fa-code")

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
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


class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/')
    url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    name = models.CharField(max_length=50, help_text="e.g. Facebook, Twitter")
    icon = models.CharField(max_length=100, help_text="Font Awesome class, e.g. fa-brands fa-facebook")
    url = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name