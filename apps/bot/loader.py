from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

token = "7293607513:AAEMbszahoLrfxC5_28fEojq0AGCkKe3EsE"
bot = Bot(token=token)
dispatcher = Dispatcher(storage=MemoryStorage())
