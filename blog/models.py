from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    summary = models.TextField()
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

