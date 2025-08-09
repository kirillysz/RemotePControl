from aiogram.types import Message

from aiogram import Router
from aiogram import F

from src.ai.ionetapi import IONetAPI
from states.ai import QuestionState

from config import config

router = Router(name="User Messages Router")
ionet = IONetAPI(api_token=config.AI_TOKEN)

@router.message(QuestionState.question)
async def send_request_to_ai(message: Message):
    question_text = message.text
    result_dict = await ionet.create_chat_completion(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        message=question_text
    )

    answer_text = result_dict['choices'][0]['message']['content']

    await message.answer(answer_text, parse_mode="Markdown")
