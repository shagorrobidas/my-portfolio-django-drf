from django.db import models


class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(
        max_length=100
    )
    end_date = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.role


class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(
        max_length=100
    )
    end_date = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.degree


class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(help_text="Percentage (0-100)")

    def __str__(self):
        return self.name
