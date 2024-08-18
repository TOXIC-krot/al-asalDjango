from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message

from asgiref.sync import sync_to_async

from apps.bot.models import TelegramUser


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> Any:

        message: Message = event
        user = message.from_user

        if not isinstance(message, Message):
            return await handler(message, data)
        if not user:
            return await handler(message, data)

        tg_user, created = await sync_to_async(TelegramUser.objects.get_or_create)(
            telegram_id=user.id,
            defaults={
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
        )

        data["tg_user"] = tg_user

        return await handler(message, data)
