from rest_framework import generics

from apps.carts.models import (
    Cart,
    CartItem,
    Order,
    OrderItem,
)
from apps.carts.serializers import (
    CartItemSerializer,
    CartSerializer,
    OrderItemSerializer,
    OrderSerializer,
)


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
