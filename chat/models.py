from django.db import models

# Create your models here.
from django.db import models

class ChatMessage(models.Model):
    room_name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
