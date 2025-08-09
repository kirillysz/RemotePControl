from aiogram.fsm.state import State, StatesGroup

class QuestionState(StatesGroup):
    question = State()