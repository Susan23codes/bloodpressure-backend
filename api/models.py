from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f'<User username={self.username} pk={self.pk}>'


class Reading(models.Model):
    systolic = models.IntegerField(blank=False, null=False)
    diastolic = models.IntegerField(blank=False, null=False)
    reading_time = models.DateTimeField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='readings')
