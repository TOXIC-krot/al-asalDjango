from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from apps.common.models import BaseModel
from apps.users.managers import UserManager

from core.validators import phone_number_validators


class UserRoleChoices(models.TextChoices):
    ADMIN = "admin", "Admin"
    WAREHOUSE = "warehouse", "Warehouse"
    DELIVERY = "delivery", "Delivery"


class User(AbstractUser, BaseModel):
    username = None
    first_name = None
    last_name = None
    email = None

    role = models.CharField(
        max_length=20, choices=UserRoleChoices.choices, default=UserRoleChoices.ADMIN
    )

    phone_number = models.CharField(
        max_length=20, validators=phone_number_validators, unique=True
    )

    def clean(self):
        phone_number = self.phone_number.replace(" ", "")
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("Такой номер уже существует.")

    def save(self, *args, **kwargs):
        self.phone_number = self.phone_number.replace(" ", "")
        super().save(*args, **kwargs)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "phone_number"

    objects = UserManager()

    def __str__(self):
        return self.phone_number
