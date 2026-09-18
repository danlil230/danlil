import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession # Новая штука для сессий
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

TOKEN = "8648914787:AAHneXWAwd9bnc9wUQ4Z7SLt_O4TWUuNgAo"

dp = Dispatcher()

# Главное меню
def get_main_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💻 Хакерский кликер", callback_data="hacker_clicker")],
        [InlineKeyboardButton(text="🖥️ Хакерский кабинет", callback_data="hacker_cabinet")],
        [InlineKeyboardButton(text="🟢 Состояние серверов", callback_data="server_status")],
        [InlineKeyboardButton(text="🎮 Каталог мини-игр", callback_data="games_menu")],
        [InlineKeyboardButton(text="💼 Бизнес-центр", callback_data="business"), 
         InlineKeyboardButton(text="🛒 Магазин скинов", callback_data="shop")],
        [InlineKeyboardButton(text="🎒 Мой рюкзак", callback_data="inventory")]
    ])
    return keyboard

# Кнопка «Назад в меню»
def get_back_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="◀️ Назад в меню", callback_data="main_menu")]
    ])
    return keyboard

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_name = message.from_user.first_name
    await message.answer(
        f"Привет, {html.bold(user_name)}! 👑 Добро пожаловать на игровую платформу Директора Дани!\n\n"
        f"💰 Золото: 0 | ⚡ Доход: +0/сек\n"
        f"🏆 Ранг: Нубик\n\n"
        f"Выбери нужный пункт в меню ниже:",
        reply_markup=get_main_keyboard()
    )

@dp.callback_query()
async def process_callbacks(callback: CallbackQuery):
    data = callback.data
    
    if data == "server_status":
        status_text = (
            "🖥️ <b>Состояние серверов платформы</b>\n\n"
            "🟢 <b>Статус:</b> Онлайн (Все системы стабильны)\n"
            "⚡ <b>Режим работы:</b> 24/7 (Облачный хостинг активен)\n"
            "🛡️ <b>Защита от DDoS:</b> Включена\n"
            "🌐 <b>Узел связи:</b> PythonAnywhere Core\n\n"
            "<i>Все сервера работают на максимальной мощности для Директора Дани!</i>"
        )
        await callback.message.edit_text(status_text, reply_markup=get_back_keyboard())

    elif data == "hacker_cabinet":
        cabinet_text = (
            "👨‍💻 <b>Хакерский кабинет Директора Дани</b>\n\n"
            "📊 Уровень доступа: <b>Главный Администратор</b>\n"
            "🛠️ Доступные модули: В разработке...\n"
            "🔒 Безопасность сессии: Максимальная\n\n"
            "<i>Здесь в будущем будут твои личные апгрейды, скрипты и инструменты взлома!</i>"
        )
        await callback.message.edit_text(cabinet_text, reply_markup=get_back_keyboard())

    elif data == "main_menu":
        user_name = callback.from_user.first_name
        menu_text = (
            f"Привет, {html.bold(user_name)}! 👑 Главное меню платформы:\n\n"
            f"💰 Золото: 0 | ⚡ Доход: +0/сек\n"
            f"🏆 Ранг: Нубик\n\n"
            f"Выбери нужный пункт в меню ниже:"
        )
        await callback.message.edit_text(menu_text, reply_markup=get_main_keyboard())

    elif data == "hacker_clicker":
        await callback.answer("Хакерский кликер скоро запустится!", show_alert=True)
    
    else:
        await callback.answer("Этот раздел находится в разработке!", show_alert=True)

async def main() -> None:
    # Создаем сессию с увеличенным таймаутом (чтобы сеть через прокси успевала обрабатываться)
    session = AiohttpSession(timeout=60)
    
    bot = Bot(
        token=TOKEN, 
        session=session,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    print("Бот успешно запущен и ждет сообщения (с учетом прокси-соединения)...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
