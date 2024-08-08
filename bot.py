import asyncio

from apps.bot.loader import bot, dispatcher
from apps.bot.handlers import router


async def main() -> None:
    try:
        dispatcher.include_routers(router)

        await bot.delete_webhook(drop_pending_updates=True)
        await dispatcher.start_polling(bot)

        print("Bot started!")
    except KeyboardInterrupt:
        print("Bot stopped manually!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
