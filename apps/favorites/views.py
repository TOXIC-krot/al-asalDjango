from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.favorites.serializers import FavoriteItemSerializer
from apps.favorites.models import Favorite, FavoriteItem
from apps.products.models import Product
    
    
class FavoriteListView(ListAPIView):
    serializer_class = FavoriteItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavoriteItem.objects.filter(saved__user=self.request.user)
        # return Favorite.objects.filter(user=self.request.user)
    

class AddToFavoritesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        favorite, created = Favorite.objects.get_or_create(user=request.user)
        
        product = Product.objects.get(id=product_id)
        favorite_item, created = FavoriteItem.objects.get_or_create(saved=favorite, product=product)

        if created:
            return Response({"message": "Product added to favorites."}, status=status.HTTP_201_CREATED)
        # impossible
        return Response({"message": "Product is already in favorites."}, status=status.HTTP_200_OK)


class RemoveFromFavoritesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        try:
            # Get the user's favorite list and the item
            favorite = Favorite.objects.get(user=request.user)
            product = Product.objects.get(id=product_id)
            favorite_item = FavoriteItem.objects.get(saved=favorite, product=product)

            # Remove the item
            favorite_item.delete()
            return Response({"message": "Product removed from favorites."}, status=status.HTTP_204_NO_CONTENT)
        except FavoriteItem.DoesNotExist:
            return Response({"error": "Product not found in favorites."}, status=status.HTTP_404_NOT_FOUND)
