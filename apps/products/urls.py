from django.urls import path
from apps.products import views


urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("category/<int:category_id>/", views.ProductListByCategoryView.as_view(), name="product_list_by_category"),
]