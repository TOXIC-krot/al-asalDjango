from rest_framework.generics import ListAPIView

from apps.favorites.serializers import (
    FavouritesSerializer
)
from apps.favorites.models import Favorite

class FavouritesView(ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavouritesSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)