from django.contrib.auth.decorators import login_required
from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
#ab models mein instead of message we will store doubts

class Profile(models.Model):
    user = models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)
    unique_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    image = models.FileField(upload_to='profile_pic', null=True,default='profile_pic/dummy-profile.png')
    last_text = models.CharField(max_length=100,null=True,blank=True)
    online_status = models.BooleanField(default=False)
    last_seen = models.DateTimeField(auto_now=True)
    is_teacher=models.BooleanField(default=False)
    is_educator=models.BooleanField(default=False)
    is_student=models.BooleanField(default=True)
    friends=models.ManyToManyField(User,related_name='friends',blank=True)
    teacher= models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)

class ChatRoom(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(unique=True, null=True)
    room_id = models.CharField(max_length=64) 

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message_content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    file=models.FileField(blank=True,null=True,upload_to='doubts/')
    
    class Meta:
        ordering = ['created_at',]
