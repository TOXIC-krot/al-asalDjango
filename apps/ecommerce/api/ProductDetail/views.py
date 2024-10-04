from rest_framework.generics import RetrieveAPIView
from apps.ecommerce.api.ProductDetail.serializers import ProductDetailSerializer
from apps.ecommerce.models import Product


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


__all__ = ("ProductDetailView",)
