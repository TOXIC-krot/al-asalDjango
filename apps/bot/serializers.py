from django.utils import timezone

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from apps.bot.models import TelegramUser


class CustomTokenObtainPairSerializer(serializers.Serializer):
    telegram_user_token = serializers.CharField(max_length=256)

    def validate(self, attrs):
        telegram_user_token = attrs.get("telegram_user_token")

        try:
            user = TelegramUser.objects.get(token=telegram_user_token)
        except TelegramUser.DoesNotExist:
            raise serializers.ValidationError("User not found.")

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
