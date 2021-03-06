from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Task(models.Model):
    name = models.CharField(max_length=30, unique=True)
    user = models.ForeignKey(User, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    points = models.IntegerField(default=0, null=True)

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        profile = UserProfile()
        profile.user = user
        profile.save()

post_save.connect(create_profile, sender=User)
