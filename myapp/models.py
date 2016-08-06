from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=25, unique=True)
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.name
