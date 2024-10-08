from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class PhoneNumberValidator(validators.RegexValidator):  
    # regex = r"^\+[0-9]\d{7,14}$"
    regex = r"^\+998\s?\d{2}\s?\d{3}\s?\d{2}\s?\d{2}$"

    message = _(
        "Phone number must be entered in a valid format.",
    )

phone_number_validators = [PhoneNumberValidator()]
