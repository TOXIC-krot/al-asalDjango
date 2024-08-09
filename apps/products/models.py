from django.db import models
from django.urls import reverse_lazy

from apps.common.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(BaseModel):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.PROTECT
    )

    title = models.CharField(max_length=256)
    description = models.TextField()

    image = models.ImageField(upload_to="products/")
    weight = models.DecimalField(max_digits=10, decimal_places=1)

    price = models.PositiveIntegerField(default=0)
    count = models.PositiveIntegerField(default=0)

    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title
