from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    WebAppInfo,
)

contact_keyboard = ReplyKeyboardMarkup(
    keyboard=[ # I think one [] is extra
        [
            KeyboardButton(
                text="Kontaktni yuborish",
                request_contact=True,
            ),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

webapp_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="BIZNING MAHSULOTLAR",
                web_app=WebAppInfo(url="https://www.al-asal.uz/products/"),
            )
        ]
    ]
)

location_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="📍 Lokatsiyani yuborish",
                request_location=True,
            ),
        ],
    ],
    resize_keyboard=True,
)
