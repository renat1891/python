import asyncio
from datetime import datetime, timedelta
import aiohttp

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = "8462311437:AAEsjq9Yol5RFmOq0YGkVZlup1z5jsm4rFw"

BASE_URL = "https://www.pravda.com.ua/news/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

categories = [
    "business", "entertainment", "general",
    "health", "science", "sports",
    "technology"
]


# category_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text=cat.capitalize(), callback_data=cat)]
#         for cat in categories
#     ]
# )


# async def send_articles(chat_id, articles):
#     if not articles:
#         await bot.send_message(chat_id, "No articles found.")
#         return

#     for article in articles[:5]:
#         text = (
#             f"<b>{article['title']}</b>\n\n"
#             f"{article.get('description', 'No description')}\n\n"
#             f"{article['url']}"
#         )
#         await bot.send_message(chat_id, text, parse_mode="HTML")


# @dp.message(Command("start"))
# async def start_command(message: types.Message):
#     subscribers.add(message.chat.id)
#     await message.answer(
#         "Welcome!\nSelect a news category:",
#         reply_markup=category_keyboard
#     )


async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())