from django.urls import path

from apps.products.views import ProductListView, ProductDetailView, CategoryListView

urlpatterns = [
    path("", ProductListView.as_view()),
    path("categories/", CategoryListView.as_view()),
    path("categories/<int:category_id>/", ProductListView.as_view()),
    path("<int:pk>/", ProductDetailView.as_view()),
]
