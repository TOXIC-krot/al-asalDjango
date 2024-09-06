from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.favorites.serializers import FavoriteSerializer
from apps.favorites.models import Favorite

    
class FavoriteListView(ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)