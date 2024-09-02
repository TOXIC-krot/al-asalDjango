from rest_framework import serializers

from apps.cart.models import (
    Cart,
    CartItem,
    Order,
    OrderItem,
)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "status",
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "id",
            "order",
            "product",
            "price",
            "count",
        )


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            "id",
            "user",
        )


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            "id",
            "cart",
            "product",
            "count",
        )
