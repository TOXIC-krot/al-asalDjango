from django.contrib import admin
from apps.favourites.models import Favorite, FavoriteItem

admin.site.register(Favorite)
admin.site.register(FavoriteItem)
