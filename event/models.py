from django.db import models
from post.models import Category, Tag

# Create your models here.

class Event(models.Model):
    #Primary Key implicit
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    description = models.TextField(null=True)
    event_categories = models.ManyToManyField(Category)
    event_tags = models.ManyToManyField(Tag)
