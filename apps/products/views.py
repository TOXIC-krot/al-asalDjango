from django.views import generic

from apps.products import models


class ProductListView(generic.ListView):
    model = models.Product
    template_name = "products/products_list.html"
    context_object_name = "products"
