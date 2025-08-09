from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from aiogram import Router
from aiogram import F

from handlers.pc_functions.funcs import CallbacksPCFunctions
from states.ai import QuestionState

router = Router(name="Callbacks Router")
callbacks = CallbacksPCFunctions()

@router.callback_query(F.data != "ai_chat")
async def handle_callback(callback: CallbackQuery):
    await callbacks.handle_action(callback)


@router.callback_query(F.data == "ai_chat")
async def handle_chat(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Выбран: Чат с Llama-4-Maverick-17B-128E-Instruct-FP8!\nПиши вопрос.")
    await state.set_state(QuestionState.question)
