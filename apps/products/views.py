# from django.views import generic
# from apps.products import models
# from apps.bot.models import TelegramUser


# class ProductListView(generic.ListView):
#     model = models.Product
#     template_name = "products/product_list.html"
#     context_object_name = "products"

#     def get_queryset(self):
#         category_id = self.kwargs.get("category_id")
#         if category_id:
#             return models.Product.objects.filter(
#                 category_id=category_id, is_available=True
#             )
#         return models.Product.objects.filter(is_available=True)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["categories"] = models.Category.objects.all()

#         telegram_user_token = self.kwargs.get("telegram_user_token")

#         if telegram_user_token:
#             context["telegram_user"] = TelegramUser.objects.get(
#                 token=telegram_user_token
#             )

#         return context


# class ProductDetailView(generic.DetailView):
#     model = models.Product
#     template_name = "products/product_detail.html"
#     context_object_name = "product"


# __all__ = (
#     "ProductListView",
#     "ProductDetailView",
# )

from rest_framework.generics import ListAPIView
from apps.products.serializers import ProductListSerializer
from apps.products.models import Product


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
