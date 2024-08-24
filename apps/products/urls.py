from django.urls import path

# from apps.products import views

from apps.products.views import ProductListView

urlpatterns = [
    # path("", views.ProductListView.as_view(), name="product_list"),
    # path(
    #     "<str:telegram_user_token>/",
    #     views.ProductListView.as_view(),
    #     name="product_list",
    # ),
    # path(
    #     "category/<int:category_id>/",
    #     views.ProductListView.as_view(),
    #     name="product_list_by_category",
    # ),
    # path("<int:pk>", views.ProductDetailView.as_view(), name="product_detail"),
    path("", ProductListView.as_view(), name="product_list"),
]
