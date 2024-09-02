from django.contrib import admin
from apps.carts.models import Cart, CartItem

admin.site.register(Cart)
admin.site.register(CartItem)
