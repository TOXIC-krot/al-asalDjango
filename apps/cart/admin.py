from django.contrib import admin
from apps.cart.models import (
    Cart,
    CartItem,
    Order,
    OrderItem,
    Saved,
    SavedItem,
)

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Saved)
admin.site.register(SavedItem)
