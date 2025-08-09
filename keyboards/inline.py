from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💻 Управление ПК", callback_data="pc_menu")],
        [InlineKeyboardButton(text="🤖 Чат с ИИ", callback_data="ai_chat")]
    ]
)

pc_control_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📂 Открыть программу", callback_data="open_menu")],
        [InlineKeyboardButton(text="❌ Закрыть программу", callback_data="close_menu")],
        [InlineKeyboardButton(text="🔌 Выключить ПК", callback_data="shutdown")],
        [InlineKeyboardButton(text="♻ Перезагрузить ПК", callback_data="reboot")],
        [InlineKeyboardButton(text="💤 Сон", callback_data="sleep")],
        [InlineKeyboardButton(text="⬅ Назад", callback_data="main_menu")]
    ]
)

open_program_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📝 Блокнот", callback_data="open_notepad")],
        [InlineKeyboardButton(text="🖩 Калькулятор", callback_data="open_calc")],
        [InlineKeyboardButton(text="🌐 Браузер", callback_data="open_browser")],
        [InlineKeyboardButton(text="⬅ Назад", callback_data="pc_menu")]
    ]
)

close_program_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📝 Блокнот", callback_data="close_notepad")],
        [InlineKeyboardButton(text="🖩 Калькулятор", callback_data="close_calc")],
        [InlineKeyboardButton(text="🌐 Браузер", callback_data="close_browser")],
        [InlineKeyboardButton(text="⬅ Назад", callback_data="pc_menu")]
    ]
)