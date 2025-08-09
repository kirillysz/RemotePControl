from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

from keyboards.inline import menu_kb

router = Router(name="User Commands Router")

@router.message(CommandStart())
async def greeting(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         "Добро пожаловать в бота!",
                         reply_markup=menu_kb)