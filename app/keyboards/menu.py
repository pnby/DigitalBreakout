from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.utils.enums import Transcriptions

button_1 = InlineKeyboardButton(text="Загрузить транскрипцию", callback_data=Transcriptions.load.value)
button_2 = InlineKeyboardButton(text="Мои транскрипции", callback_data=Transcriptions.view.value)

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_1, button_2]
    ]
)
