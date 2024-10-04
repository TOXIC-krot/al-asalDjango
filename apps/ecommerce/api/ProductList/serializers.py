from rest_framework import serializers
from apps.ecommerce.models import Product


class ProductListSerializer(serializers.ModelSerializer):
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


__all__ = ("ProductListSerializer",)
