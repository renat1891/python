import asyncio
from datetime import datetime, timedelta
import aiohttp

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from parsing import get_data_info
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8462311437:AAEsjq9Yol5RFmOq0YGkVZlup1z5jsm4rFw"

BASE_URL = "https://www.pravda.com.ua/news/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

categories = [
    "main","eurointegration","epravda","life","mezha","oboronka","champion"
]

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Усі Новини")]
        [KeyboardButton(text="Головне"),
            KeyboardButton(text="Політика")]
        [KeyboardButton(text="Економіка"),
            KeyboardButton(text="Життя")]
        [KeyboardButton(text="Технології"),
            KeyboardButton(text="Оборонка")]
        [KeyboardButton(text="Спорт")]
    ],
    resize_keyboard=True
)




async def send_articles(chat_id, articles):
    if not articles:
        await bot.send_message(chat_id, "No articles found.")
        return

    for article in articles[:5]:
        text = (
            f"<b>{article['title']}</b>\n\n"
            f"{article.get('description', 'No description')}\n\n"
            f"{article['url']}"
        )
        await bot.send_message(chat_id, text, parse_mode="HTML")


@dp.message(Command("start"))
async def start_command(message: types.Message):
    (message.chat.id)
    await message.answer(
        "Welcome!\nSelect a news category:",
        reply_markup=keyboard
    )


async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())