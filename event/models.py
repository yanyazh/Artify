from django.db import models
from post.models import Category, Tag
from user.models import User

# Create your models here.

class Event(models.Model):
    #Primary Key implicit
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    description = models.TextField(null=True)
    # Foreign key
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # Many-to-many relations
    event_categories = models.ManyToManyField(Category, blank=True)
    event_tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f" Event: {self.id} - {self.title}"
