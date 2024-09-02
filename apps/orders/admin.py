from django.contrib import admin
from apps.orders.models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
