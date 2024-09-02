from django.db import models

from apps.common.models import BaseModel
from apps.products.models import Product
from apps.users.models import User


"""
OrderStatusChoices
Order
OrderItem
Cart
CartItem
"""


class OrderStatusChoices(models.TextChoices):
    PENDING = "PENDING", "Pending"
    CONFIRMED = "CONFIRMED", "Confirmed"
    CANCELLED = "CANCELLED", "Cancelled"
    DELIVERED = "DELIVERED", "Delivered"


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.PENDING,
    )


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    count = models.PositiveIntegerField(default=1)


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    count = models.PositiveIntegerField(default=1)
