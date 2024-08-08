import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ContentType,
    Message,
    WebAppInfo,
    ReplyKeyboardRemove,
)
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F

bot_token = "7293607513:AAEMbszahoLrfxC5_28fEojq0AGCkKe3EsE"
bot = Bot(token=bot_token)
dp = Dispatcher(storage=MemoryStorage())

# Keyboards
contact_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[KeyboardButton(text="Kontaktni yuborish", request_contact=True)]],
)

web_app_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Bizning sahifamizga utish",
                web_app=WebAppInfo(url="https://www.al-asal.uz/"),
            )
        ]
    ]
)

location_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[KeyboardButton(text="📍 Lokatsiyani yuborish", request_location=True)]],
)


@dp.message(Command("start"))
async def start(message: Message):
    photo_url = "https://heartfelt-cascaron-a8b855.netlify.app/assets/logo.jpg"
    caption_text = (
        'AsSalomu alaykum! "Al-asal" sahifamizga hush kelibsiz, '
        "tizimni ishga tushirish uchun kelin tanishib olaylik, uning uchun, "
        "o`z kontaktingizni junating."
    )
    await message.answer_photo(
        photo=photo_url, caption=caption_text, reply_markup=contact_kb
    )


@dp.message(F.contact)
async def cmd_contact(message: Message):
    await message.answer(
        "Bizning sahifamizga utish uchun quyidagi tugmani bosing:",
        reply_markup=web_app_button,
    )
    await message.answer("Iltimos, lokatsiyangizni yuboring:", reply_markup=location_kb)


@dp.message(F.location)
async def handle_location(message: Message):
    await message.answer(
        "Sizning manzilingiz qabul qilindi. Operatorlarimiz 24 soat ichida siz bilan bog'lanadi.",
        reply_markup=ReplyKeyboardRemove(),
    )


async def main() -> None:
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print("Bot stopped manually")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
