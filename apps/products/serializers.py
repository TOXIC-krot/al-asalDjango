from rest_framework.serializers import ModelSerializer
from apps.products.models import Product


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
