from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.utils.enums import Transcriptions

button_1 = InlineKeyboardButton(text="Загрузить документ", callback_data=Transcriptions.load.value)
button_2 = InlineKeyboardButton(text="Мои транскрипции", callback_data=Transcriptions.view.value)

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_1, button_2]
    ]
)

back_button = InlineKeyboardButton(text="◀️ Назад", callback_data=Transcriptions.back.value)
build_proto_button = InlineKeyboardButton(text="Сформировать протокол", callback_data=Transcriptions.build_proto.value)
build_assignment_button = InlineKeyboardButton(text="Сформировать поручения", callback_data=Transcriptions.build_assignments.value)

protocol_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [build_proto_button, build_assignment_button],
        [back_button]
    ]
)
