from django.urls import path
from apps.favorites.views import FavoriteListView

urlpatterns = [
    path("", FavoriteListView.as_view()),
]
