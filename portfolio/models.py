# Create your models here.
from django.db import models

# Apna Project Model
class Project(models.Model):
    title = models.CharField(max_length=100)            # Project name
    description = models.TextField()                    # Project detail
    github_link = models.URLField()                     # GitHub ka link
    tech_stack = models.CharField(max_length=100)       # Unique feature: stack info
    likes = models.IntegerField(default=0)              # Unique feature: like counter

    def __str__(self):
        return self.title
