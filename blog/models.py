from django.db import models
from mdeditor.fields import MDTextField


class Post(models.Model):
    slug = models.CharField(max_length=255,unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(max_length=500)
    body = MDTextField()

