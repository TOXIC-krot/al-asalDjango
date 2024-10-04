from django.urls import path
from .api import *


urlpatterns = [
    path("products/", ProductListView.as_view(), "product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), "product-detail"),
]
