from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"


class Project(models.Model):
    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(
        Category,
        related_name='projects'
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True
    )
    tags = models.CharField(
        max_length=200,
        help_text="Comma separated tags"
    )
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    
    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',')]

    def __str__(self):
        return self.title