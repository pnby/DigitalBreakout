from aiogram.fsm.state import StatesGroup, State


class TranscriptionStates(StatesGroup):
    LOAD = State()