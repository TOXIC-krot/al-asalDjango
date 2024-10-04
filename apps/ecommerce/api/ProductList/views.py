from rest_framework.generics import ListAPIView
from apps.ecommerce.api.ProductList.serializers import ProductListSerializer
from apps.ecommerce.models import Product


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


__all__ = ("ProductListView",)
