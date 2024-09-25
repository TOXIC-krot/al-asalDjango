from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models import Q

from apps.products.serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    CategoryListSerializer,
)
from apps.products.models import Product, Category


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = (AllowAny,)


class ProductListView(ListAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get("category_id")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        search_term = self.request.query_params.get("search")
        if search_term:
            queryset = queryset.filter(title__istartswith=search_term)
        return queryset


class ProductSearchView(ListAPIView):
    permission_classes = (AllowAny,)


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = (AllowAny,)


__all__ = (
    "ProductListView",
    "ProductSearchView",
    "ProductDetailView",
    "CategoryListView",
)
