from aiogram.types import CallbackQuery
from src.pc.utils import PCUtils

from keyboards.inline import menu_kb, pc_control_kb, open_program_kb, close_program_kb

pc = PCUtils()

class CallbacksPCFunctions:
    def __init__(self):
        self.callback_actions = {
            "open_notepad": ("open_app", "notepad.exe", "Открываю Блокнот ✅", "Не удалось открыть Блокнот ❌"),
            "open_calc": ("open_app", "calc.exe", "Открываю Калькулятор ✅", "Не удалось открыть Калькулятор ❌"),
            "open_browser": ("open_app", r"C:\Program Files\Firefox Nightly\firefox.exe", "Открываю Браузер ✅", "Не удалось открыть Браузер ❌"),

            "close_notepad": ("close_app", "notepad.exe", "Закрываю Блокнот ✅", "Не удалось закрыть Блокнот ❌"),
            "close_calc": ("close_app", "calc.exe", "Закрываю Калькулятор ✅", "Не удалось закрыть Калькулятор ❌"),
            "close_browser": ("close_app", "firefox.exe", "Закрываю Браузер ✅", "Не удалось закрыть Браузер ❌"),
        }

        self.menu_actions = {
            "main_menu": (self.show_main_menu, menu_kb),
            "pc_menu": (self.show_pc_menu, pc_control_kb),
            "open_menu": (self.show_open_menu, open_program_kb),
            "close_menu": (self.show_close_menu, close_program_kb),
            "shutdown": (self.shutdown_pc, None),
            "reboot": (self.reboot_pc, None),
            "sleep": (self.sleep_pc, None),
        }


    async def handle_action(self, callback: CallbackQuery):
        data = callback.data

        if data in self.menu_actions:
            handler, keyboard = self.menu_actions[data]
            if keyboard:
                await callback.message.edit_text(f"Выбрано: {data.replace('_', ' ').capitalize()}", reply_markup=keyboard)
            else:
                await handler(callback)
            return
        
        if data in self.callback_actions:
            method_name, app_path, success_message, error_message = self.callback_actions[data]
            method = getattr(pc, method_name, None)
            
            if not method:
                await callback.answer("Метод не найден ❌", show_alert=True)
                return
            
            result = method(app_path)

            await callback.answer(success_message if result else error_message, show_alert=True)
            return
        
        await callback.answer("Неизвестная команда ❌", show_alert=True)


    async def show_main_menu(self, callback: CallbackQuery):
        await callback.message.edit_text("Выбери действие:", reply_markup=menu_kb)

    async def show_pc_menu(self, callback: CallbackQuery):
        await callback.message.edit_text("Управление ПК:", reply_markup=pc_control_kb)

    async def show_open_menu(self, callback: CallbackQuery):
        await callback.message.edit_text("Выбери программу для открытия:", reply_markup=open_program_kb)

    async def show_close_menu(self, callback: CallbackQuery):
        await callback.message.edit_text("Выбери программу для закрытия:", reply_markup=close_program_kb)

    async def shutdown_pc(self, callback: CallbackQuery):
        if pc.shutdown():
            await callback.answer("Выключаю ПК...", show_alert=True)
        else:
            await callback.answer("Не удалось выключить ПК ❌", show_alert=True)

    async def reboot_pc(self, callback: CallbackQuery):
        if pc.reboot():
            await callback.answer("Перезагрузка ПК...", show_alert=True)
        else:
            await callback.answer("Не удалось перезагрузить ПК ❌", show_alert=True)

    async def sleep_pc(self, callback: CallbackQuery):
        if pc.sleep():
            await callback.answer("Перевожу в спящий режим...", show_alert=True)
        else:
            await callback.answer("Не удалось перевести в спящий режим ❌", show_alert=True)