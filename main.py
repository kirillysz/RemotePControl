from aiogram import Bot, Dispatcher

from asyncio import run
from config import config

from src.log.logging import _logger

from handlers.user_commands import router as commands_router
from handlers.user_messages import router as messages_router
from handlers.callbacks import router as callbacks_router

async def main():
    bot = Bot(config.BOT_TOKEN)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(
        commands_router,
        messages_router,
        callbacks_router
    )
    
    _logger.info(msg="Бот запущен.")
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    run(main())