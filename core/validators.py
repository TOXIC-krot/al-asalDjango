from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class PhoneNumberValidator(validators.RegexValidator):
    regex = r"^\+998(3[0-9]|9[0-3])\d{7}$"

    message = _(
        "Phone number must be entered in a valid format. (e.g. +998991234567)",
    )


phone_number_validators = [PhoneNumberValidator()]
