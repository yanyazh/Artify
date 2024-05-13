from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.

class CustomUser(AbstractUser):
    first_name = None
    last_name = None

    def __str__(self):
        return self.username

class Follower(models.Model):
    follow_date = models.DateTimeField(default=timezone.now)
    #Foreign Keys
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='target')
    follower_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='follower')
    #Composite primary key
    class Meta:
        unique_together = ('user_id', 'follower_id')

    def __str__(self):
        return f"Follow from {self.follower_id} to {self.user_id}"
        