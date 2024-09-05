from rest_framework.serializers import ModelSerializer
from apps.favorites.models import Favorite


class FavouritesSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = (
            "id",
            "category",
            "title",
            "description",
            "image",
            "weight",
            "video_url",
            "price",
            "count",
        )
