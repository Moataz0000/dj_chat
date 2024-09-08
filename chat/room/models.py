from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def get_room_url(self):
        return reverse('room_detail', args=[self.slug])



class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.content[:20]


    class Meta:
        ordering = ['date_added']