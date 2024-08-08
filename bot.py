import asyncio

from apps.bot.loader import bot, dispatcher


async def main() -> None:
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dispatcher.start_polling(bot)
    except KeyboardInterrupt:
        print("Bot stopped manually")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
