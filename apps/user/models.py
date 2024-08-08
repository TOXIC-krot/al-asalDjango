from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    registered_at = models.DateTimeField(auto_now_add=True)
    last_active_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user_id}"
