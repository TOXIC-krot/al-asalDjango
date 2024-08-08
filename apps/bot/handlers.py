from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from apps.bot.loader import dispatcher
from apps.bot.keyboards import contact_keyboard, location_keyboard, webapp_keyboard


@dispatcher.message(Command("start"))
async def start_handler(message: Message):
    photo_url = "https://heartfelt-cascaron-a8b855.netlify.app/assets/logo.jpg"
    caption_text = (
        'AsSalomu alaykum! "Al-asal" sahifamizga hush kelibsiz, '
        "tizimni ishga tushirish uchun kelin tanishib olaylik, uning uchun, "
        "o`z kontaktingizni junating."
    )
    await message.answer_photo(
        photo=photo_url, caption=caption_text, reply_markup=contact_keyboard
    )


@dispatcher.message(F.contact)
async def contact_handler(message: Message):
    await message.answer(
        "Mahsulotlarni ko'rish uchun tugmani bosing!",
        reply_markup=webapp_keyboard,
    )
    await message.answer(
        "Iltimos, lokatsiyangizni yuboring:", reply_markup=location_keyboard
    )


@dispatcher.message(F.location)
async def location_handler(message: Message):
    await message.answer(
        "Sizning manzilingiz qabul qilindi. Operatorlarimiz 24 soat ichida siz bilan bog'lanadi.",
        reply_markup=ReplyKeyboardRemove(),
    )
