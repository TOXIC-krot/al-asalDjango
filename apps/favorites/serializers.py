from rest_framework.serializers import ModelSerializer
from apps.favorites.models import Favorite, FavoriteItem
from apps.products.serializers import ProductListSerializer


class FavoriteItemSerializer(ModelSerializer):
    product = ProductListSerializer(read_only=True)

    class Meta:
        model = FavoriteItem
        fields = ['id', 'product']

class FavoriteSerializer(ModelSerializer):
    items = FavoriteItemSerializer(source='favoriteitem_set', many=True, read_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'items']