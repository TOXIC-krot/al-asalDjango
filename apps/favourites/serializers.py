from rest_framework.serializers import ModelSerializer
from apps.favourites.models import Favourites


class FavouritesSerializer(ModelSerializer):
    class Meta:
        model = Favourites
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
