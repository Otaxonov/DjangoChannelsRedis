from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['time_sent']
