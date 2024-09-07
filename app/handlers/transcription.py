from typing import Optional, cast, List

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message, Audio

from app.database.models.meetings.protocol import Protocol
from app.database.models.meetings.user import User
from app.keyboards.menu import protocol_keyboard
from app.states.transcription import TranscriptionStates
from app.utils.enums import Transcriptions
from app.utils.utils import safe_download, create_paginated_keyboard, format_protocol

router = Router()

@router.callback_query(F.data.startswith(Transcriptions.load.value))
async def process_transcriptions_send(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Ожидаю...")
    await state.set_state(TranscriptionStates.LOAD)


@router.message(TranscriptionStates.LOAD)
async def process_transcription_load(message: Message, state: FSMContext):
    audio: Audio = message.audio
    if audio is None:
        await message.answer("Пожалуйста, загрузите mp3 файл.")
        return
    if audio.mime_type == "audio/mpeg":
        await message.answer("Файл принят. Обрабатываю транскрипцию...")
        file_id = audio.file_id
        file = await message.bot.get_file(file_id)
        await safe_download(file)
    else:
        await message.answer("Пожалуйста, загрузите mp3 файл.")
    await state.clear()


@router.callback_query(F.data.startswith(Transcriptions.view.value))
async def process_transcriptions_view(callback_query: CallbackQuery, state: FSMContext):
    user: Optional[User] = await User.find_one(User.telegram_id == callback_query.from_user.id, fetch_links=True)
    if user is None or user.protocols is None:
        await callback_query.answer("Похоже у вас нету ни одной транскрипции")
        return

    protocols = cast(list[Protocol], user.protocols)
    protocol_titles = sorted([protocol.title for protocol in protocols])

    keyboard = create_paginated_keyboard(protocol_titles)
    await state.update_data(all_items=protocol_titles)

    await callback_query.message.answer("Ваши транскрипции:", reply_markup=keyboard)


@router.callback_query(F.data.startswith(Transcriptions.page.value))
async def process_page_change(callback_query: CallbackQuery, state: FSMContext):
    page = int(callback_query.data.split(':')[1])
    data = await state.get_data()
    all_items = data.get('all_items', [])

    keyboard = create_paginated_keyboard(all_items, page)
    await callback_query.message.edit_reply_markup(reply_markup=keyboard)


@router.callback_query(F.data.startswith(Transcriptions.item.value))
async def on_subject_choice(callback_query: CallbackQuery):
    callback_data = callback_query.data.split(':')[1]
    user = await User.find_one(User.telegram_id == callback_query.from_user.id, fetch_links=True)
    assert user is not None
    user = cast(User, user)
    protocols = cast(List[Protocol], user.protocols)

    selected_protocol = None
    for protocol in protocols:
        if protocol.title == callback_data:
            selected_protocol = protocol
            break

    if selected_protocol:
        formatted_message = format_protocol(selected_protocol)

        await callback_query.message.edit_text(formatted_message, parse_mode="HTML", reply_markup=protocol_keyboard)
        await callback_query.answer(f"Вы выбрали {selected_protocol.title}")
    else:
        await callback_query.answer("Протокол не найден.", show_alert=True)


@router.callback_query(F.data.startswith(Transcriptions.back.value))
async def back_to_list(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    all_items = data.get('all_items', [])

    keyboard = create_paginated_keyboard(all_items)
    await callback_query.message.edit_text("Ваши транскрипции:", reply_markup=keyboard)
    await callback_query.answer()
