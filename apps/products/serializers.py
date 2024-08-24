from rest_framework.serializers import ModelSerializer
from apps.products.models import Product, Category


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
        )


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "image",
            "price",
            "weight",
            "count",
        )


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "title",
            "description",
            "image",
            "weight",
            "video_url",
            "price",
            "count",
        )
