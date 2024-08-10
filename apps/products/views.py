from django.views import generic
from apps.products import models


class ProductListView(generic.ListView):
    model = models.Product
    template_name = "products/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        if category_id:
            return models.Product.objects.filter(category_id=category_id)
        return models.Product.objects.all()


class ProductDetailView(generic.DetailView):
    model = models.Product
    template_name = "products/product_detail.html"
    context_object_name = "product"


__all__ = (
    "ProductListView",
    "ProductDetailView",
)
