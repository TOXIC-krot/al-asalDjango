from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

bot_token = "7103058255:AAEgd6zSw9PAvwneoCJ3OD0K2jEO4FUSnAo"
bot = Bot(bot_token)
dp = Dispatcher(bot)

# Keyboards
contact = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Kontaktni yuborish", request_contact=True)
)

# Web App Button
web_app_button = InlineKeyboardMarkup().add(
    InlineKeyboardButton(
        "Bizning sahifamizga utish",
        web_app=types.WebAppInfo(url="https://www.al-asal.uz/"),
    )
)

location_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("📍 Lokatsiyani yuborish", request_location=True)
)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):

    await bot.send_message(chat_id=message.chat.id, text="hereee")

    photo_url = "https://heartfelt-cascaron-a8b855.netlify.app/assets/logo.jpg"
    caption_text = (
        'AsSalomu alaykum! "Al-asal" sahifamizga hush kelibsiz, '
        "tizimni ishga tushirish uchun kelin tanishib olaylik, uning uchun, "
        "o`z kontaktingizni junating."
    )
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption=caption_text,
        reply_markup=contact,
    )


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def cmd_contact(message: types.Message):
    await message.answer(
        "Bizning sahifamizga utish uchun quyidagi tugmani bosing:",
        reply_markup=web_app_button,
    )
    await message.answer("Iltimos, lokatsiyangizni yuboring:", reply_markup=location_kb)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def handle_location(message: types.Message):
    await message.answer(
        "Sizning manzilingiz qabul qilindi. Operatorlarimiz 24 soat ichida siz bilan bog'lanadi.",
        reply_markup=types.ReplyKeyboardRemove(),
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
