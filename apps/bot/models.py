from django.db import models

from apps.common.models import BaseModel


class TelegramUser(BaseModel):
    telegram_id = models.PositiveIntegerField(unique=True)

    username = models.CharField(max_length=256, blank=True, null=True)
    first_name = models.CharField(max_length=256, blank=True, null=True)
    last_name = models.CharField(max_length=256, blank=True, null=True)

    token = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
