from django.contrib import admin
from apps.favorites.models import Favorite, FavoriteItem

admin.site.register(Favorite)
admin.site.register(FavoriteItem)
