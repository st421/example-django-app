from django.db import models

class Task(models.Model):
    name = models.TextField(max_length=25, unique=True)

    def __str__(self):
        return self.name
