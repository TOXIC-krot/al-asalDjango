from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User


class Category(BaseModel):
    title = models.CharField(max_length=256)


class Product(BaseModel):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.PROTECT
    )

    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="products/")
    price = models.PositiveIntegerField(default=0)
    count = models.PositiveIntegerField(default=0)
    description = models.TextField()

    is_available = models.BooleanField(default=True)


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
