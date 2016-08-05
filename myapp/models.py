from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, null=True)
    name = models.TextField(max_length=25, unique=True)

    def __str__(self):
        return self.name
