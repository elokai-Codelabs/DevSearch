from django.db import models
from django.contrib.auth.models import User
import uuid

# SIGNALS MODELS



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200, blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    username = models.CharField(max_length=200, blank=True,null=True)
    location = models.CharField(max_length=200, blank=True,null=True)
    short_intro = models.CharField(max_length=200,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True,upload_to = 'profiles/',default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, blank=True,null=True)
    social_twitter = models.CharField(max_length=200, blank=True,null=True)
    social_linkedin = models.CharField(max_length=200, blank=True,null=True)
    social_youtube = models.CharField(max_length=200, blank=True,null=True)
    social_website = models.CharField(max_length=200, blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False,primary_key=True)

    def __str__(self):
        # return str(self.user.username)
        return str(self.username)

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=600, blank=True,null=True)
    description = models.TextField(max_length=600, blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, editable=False,primary_key=True)
    
    def __str__(self):
        return str(self.name)




