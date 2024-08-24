from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.common.models import BaseModel
from apps.users.managers import UserManager

from core.validators import phone_number_validators


class User(AbstractUser, BaseModel):
    username = None
    first_name = None
    last_name = None
    email = None

    phone_number = models.CharField(
        max_length=32, validators=phone_number_validators, unique=True
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "phone_number"

    objects = UserManager()

    def __str__(self):
        return self.phone_number
