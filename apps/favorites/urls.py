from django.urls import path
from apps.favorites.views import FavoriteListView, AddToFavoritesView, RemoveFromFavoritesView

urlpatterns = [
    path("", FavoriteListView.as_view()),
    path("add/<int:product_id>/", AddToFavoritesView.as_view()),
    path("remove/<int:product_id>/", RemoveFromFavoritesView.as_view()),
]
