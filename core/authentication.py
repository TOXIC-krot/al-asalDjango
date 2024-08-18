from django.utils import timezone

from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.bot.models import TelegramUser


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        user = self.get_user(validated_token)

        if user is None:
            raise AuthenticationFailed("User not found.")

        return (user, validated_token)

    def get_user(self, validated_token):
        telegram_user_token = validated_token.get("telegram_user_token")

        try:
            user = TelegramUser.objects.get(token=telegram_user_token)
        except TelegramUser.DoesNotExist:
            raise AuthenticationFailed("User not found.")

        return user
