import asyncio
from datetime import datetime, timedelta
import aiohttp

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


API_KEY = ""
TOKEN = "8462311437:AAEsjq9Yol5RFmOq0YGkVZlup1z5jsm4rFw"

BASE_URL = "https://newsapi.org/v2/top-headlines"

bot = Bot(token=TOKEN)
dp = Dispatcher()

categories = [
    "business", "entertainment", "general",
    "health", "science", "sports",
    "technology"
]


category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=cat.capitalize(), callback_data=cat)]
        for cat in categories
    ]
)

subscribers = set()


async def fetch_news(category):
    params = {
        "apiKey": API_KEY,
        "category": category,
        "country": "us"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as response:
            data = await response.json()
            return data.get("articles", [])


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
    subscribers.add(message.chat.id)
    await message.answer(
        "Welcome!\nSelect a news category:",
        reply_markup=category_keyboard
    )


@dp.callback_query()
async def category_selected(callback: types.CallbackQuery):
    category = callback.data

    await callback.message.edit_text(
        f"Fetching news: <b>{category.capitalize()}</b>",
        parse_mode="HTML"
    )

    articles = await fetch_news(category)
    await send_articles(callback.message.chat.id, articles)


async def auto_news_sender():
    """
    Надсилає новини всім підписникам кожну хвилину
    """
    interval = timedelta(minutes=1)
    next_run = datetime.now()

    while True:
        if datetime.now() >= next_run:
            print("Sending scheduled news...")

            for user_id in subscribers:
                articles = await fetch_news("general")
                await send_articles(user_id, articles)

            next_run = datetime.now() + interval

        await asyncio.sleep(1)


async def main():
    print("Bot started...")
    asyncio.create_task(auto_news_sender())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())