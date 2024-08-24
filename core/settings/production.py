from core.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
    "admin.al-asal.uz",
]

CSRF_TRUSTED_ORIGINS = [
    "https://admin.al-asal.uz",
]
CSRF_COOKIE_SECURE = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASS"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    }
}

LOGGER_BOT_TOKEN = env.str("LOGGER_BOT_TOKEN")
LOGGER_CHAT_ID = env.str("LOGGER_CHAT_ID")

CORS_ALLOWED_ORIGINS = [
    "https://www.al-asal.uz",
    "https://al-asal-frontend.vercel.app/",
]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
