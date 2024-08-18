from django.conf import settings

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(storage=MemoryStorage())
