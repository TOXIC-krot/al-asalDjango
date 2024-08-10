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


class ProductListByCategoryView(generic.ListView):
    model = models.Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    
    def get_queryset(self):
        category_id = self.kwargs["category_id"]
        return models.Product.objects.filter(category_id=category_id)


__all__ = (
    "ProductListView",
    "ProductDetailView",
)