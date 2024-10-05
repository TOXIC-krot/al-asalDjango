from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

from core.validators import phone_number_validators

from apps.users.managers import UserManager
from apps.common.models import BaseModel


class User(AbstractUser, BaseModel):
    username = None
    first_name = None
    last_name = None
    email = None

    phone_number = models.CharField(
        max_length=20, validators=phone_number_validators, unique=True
    )

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "phone_number"

    objects = UserManager()

    def __str__(self):
        return self.phone_number
