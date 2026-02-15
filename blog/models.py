from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)
    date = models.DateField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    summary = models.TextField()
    content = models.TextField(blank=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
