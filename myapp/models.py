from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=30, unique=True)
    user = models.ForeignKey(User, null=True)
