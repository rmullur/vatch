import os
import time
import uuid
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Generate a uuid
def _createid():
    unique_id = str(uuid.uuid4())
    unique_id.replace("-", "_")
    return unique_id

#Model which will refer to a video by a user
class Video(models.Model):
    username     = models.ForeignKey(User,on_delete=models.CASCADE,blank = False,primary_key=True)
    video_title  = models.CharField(max_length=500,default = "Untitled")
    video_url    = models.URLField(max_length=500, blank = False, default = "NULL")
    stream_key   = models.CharField(max_length=500)
    views        = models.IntegerField(default = 0)
    thumbnail    = models.ImageField(upload_to=None, height_field=None, width_field=None)
    live         = models.BooleanField(default = False)
    active       = models.BooleanField(default = False)

    def _str_(self):
       return self.username

class UserProfile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,blank=False,primary_key=True)
    picture  = models.ImageField(upload_to=None, height_field=None, width_field=None)
    bio      = models.CharField(max_length=500)


#Extending existing Django User Profile for Stream Key
class Profile(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
     user_streamkey     = models.CharField(max_length=500)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
     if created:
         Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
     instance.profile.user_streamkey=_createid()
     instance.profile.save()

     def _str_(self):
       return self.user_streamkey
