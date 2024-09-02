from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.products.models import Product
from apps.users.models import User


class Favorite(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Saved")
        verbose_name_plural = _("Saved")


class FavoriteItem(BaseModel):
    saved = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Saved Item")
        verbose_name_plural = _("Saved Items")


__all__ = (
    "Favorite",
    "FavoriteItem",
)
