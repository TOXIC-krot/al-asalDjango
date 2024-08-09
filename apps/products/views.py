from django.views import generic
from apps.products import models


class ProductListView(generic.ListView):
    model = models.Product
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProductDetailView(generic.DetailView):
    model = models.Product
    template_name = "products/product_detail.html"
    context_object_name = "product"


__all__ = (
    "ProductListView",
    "ProductDetailView",
)
