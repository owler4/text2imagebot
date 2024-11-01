from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from models import MODELS

HELP = """
Для генерации изображения ответь командой /promt на сообщение с промтом
"""

START_STRING = """ **Доброго времени суток, {}!**
Я работаю в тестовом режиме

Для генерации изображения ответь командой /promt на сообщение с промтом
"""

ABOUT = """
● **LIBRARY :** `Pyrogram` 
● **LANGUAGE :** `Python 3.10` 
"""

START_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ОБО МНЕ", callback_data="cbabout"),
            InlineKeyboardButton("ПОМОЩЬ", callback_data="cbhelp"),
        ],
        [InlineKeyboardButton("НАСТРОЙКИ", callback_data="cbsettings")],
        [
            InlineKeyboardButton("↗ Join Here ↗", url="https://t.me/BughunterBots"),
        ],
    ]
)
CLOSE_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Назад", callback_data="cbclose"),
        ]
    ]
)


BACK = [InlineKeyboardButton("НАЗАД", callback_data="back")]


SETTINGS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Выбрать модель", callback_data="choose_model"),
            InlineKeyboardButton("Изменить кол-во шагов", callback_data="change_steps"),
        ],
        [
            InlineKeyboardButton("Изменить сид", callback_data="change_seed"),
            InlineKeyboardButton(
                "Изменить кол-во изображений", callback_data="change_image_count"
            ),
        ],
        [InlineKeyboardButton("Сохранить конфигурацию", callback_data="save_settings")],
    ]
)

MODELS_BUTTON = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(model, callback_data=f"select_model_{index}")]
        for index, model in enumerate(MODELS)
    ]
    + [[InlineKeyboardButton("Назад", callback_data="cb_back_settings")]]
)


STEPS_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("-", callback_data="-steps"),
            InlineKeyboardButton("+", callback_data="+steps"),
        ],
        [InlineKeyboardButton("Back", callback_data="cb_back_settings")],
    ]
)
IMAGE_COUNT_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("-", callback_data="-image"),
            InlineKeyboardButton("+", callback_data="+image"),
        ],
        [InlineKeyboardButton("Back", callback_data="cb_back_settings")],
    ]
)
