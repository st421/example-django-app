from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=75, null=True)

    def __str__(self):
        return self.name
