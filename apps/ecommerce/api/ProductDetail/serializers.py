from rest_framework import serializers
from apps.ecommerce.models import Product


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "title",
            "image",
            "price",
            "count",
            "description",
            "is_available",
        )


__all__ = ("ProductDetailSerializer",)
