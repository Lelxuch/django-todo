from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title