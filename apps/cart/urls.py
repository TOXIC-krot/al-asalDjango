from django.urls import path
from .views import *


urlpatterns = [
    path("update/", CartUpdateView.as_view(), name="update_cart"),
    path("", CartDetailView.as_view(), name="cart_detail"),
    # path("add/<int:product_id>/", cart_add, name="cart_add"),
    # path("remove/<int:product_id>/", cart_remove, name="cart_remove"),
    # path("order/", order, name="order"),
]
