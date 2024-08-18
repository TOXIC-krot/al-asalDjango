from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from apps.bot.keyboards import contact_keyboard, location_keyboard
from apps.bot.models import TelegramUser


from asgiref.sync import sync_to_async


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


import secrets


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    photo_url = "https://heartfelt-cascaron-a8b855.netlify.app/assets/logo.jpg"
    caption_text = (
        'Assalomu alaykum! "Al-asal" sahifamizga xush kelibsiz, '
        "tizimni ishga tushirish uchun keling avval tanishib olaylik, "
        "o'z kontaktingizni jo'nating."
    )
    await message.answer_photo(
        photo=photo_url, caption=caption_text, reply_markup=contact_keyboard
    )


@router.message(F.contact)
async def contact_handler(message: Message, tg_user: TelegramUser):
    # Remove the contact keyboard
    await message.answer(
        "Tabriklaymiz! Tizimdan muvaffaqiyatli ro'yxatdan o'tdingiz.",
        reply_markup=ReplyKeyboardRemove(),  # Remove the contact keyboard
    )

    token = secrets.token_urlsafe(16)
    tg_user.token = token
    await sync_to_async(tg_user.save)()

    webapp_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="BIZNING MAHSULOTLAR",
                    web_app=WebAppInfo(
                        url=f"https://www.al-asal.uz/products/{tg_user.token}/"
                    ),
                )
            ]
        ]
    )

    # Send a new message with the new webapp keyboard
    await message.answer(
        "Mahsulotlarni ko'rish uchun tugmani bosing!", reply_markup=webapp_keyboard
    )


#     await message.answer(
#         "Iltimos, lokatsiyangizni yuboring:", reply_markup=location_keyboard
#     )


# @router.message(F.location)
# async def location_handler(message: Message):
#     await message.answer(
#         "Sizning manzilingiz qabul qilindi. Operatorlarimiz 24 soat ichida siz bilan bog'lanadi.",
#         reply_markup=ReplyKeyboardRemove(),
#     )
