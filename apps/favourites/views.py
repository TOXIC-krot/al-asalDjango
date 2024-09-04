from rest_framework.generics import ListAPIView

from apps.favourites.serializers import (
    FavouritesSerializer
)
from apps.favourites.models import Favourites

class FavouritesView(ListAPIView):
    queryset = Favourites.objects.all()
    serializer_class = FavouritesSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)