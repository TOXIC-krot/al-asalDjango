import django
import environ

environ.Env.read_env(".env")
django.setup()

import asyncio

from apps.bot.loader import bot, dispatcher
from apps.bot.middlewares import AuthMiddleware
from apps.bot.handlers import router


async def on_startup(dispatcher):
    print("Bot started!")


async def main() -> None:
    try:
        dispatcher.include_routers(router)
        dispatcher.message.outer_middleware(AuthMiddleware())
        dispatcher.startup.register(on_startup)

        await bot.delete_webhook(drop_pending_updates=True)
        await dispatcher.start_polling(bot)

    except KeyboardInterrupt:
        print("Bot stopped manually!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
