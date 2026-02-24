import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
    
    
    

from parsing_workua import parse_python_jobs

TOKEN = "8534853373:AAE1sGuAR5ye4p5jDUIL6YT01gHFCE73168"

bot = Bot(TOKEN)
dp = Dispatcher()

user_data = {}

city_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kyiv"), KeyboardButton(text="Lviv")],
        [KeyboardButton(text="Remote")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Привіт.\nОберіть місто:",
        reply_markup=city_keyboard
    )

@dp.message(lambda message: message.text.lower() in ["kyiv", "lviv", "remote"])
async def send_first_job(message: types.Message):
    city = message.text.lower()

    await message.answer("Пошук вакансій...")

    jobs = parse_python_jobs(city, limit=10)

    if not jobs:
        await message.answer("Вакансій не знайдено")
        return

    user_data[message.from_user.id] = {
        "jobs": jobs,
        "index": 0
    }

    await send_job(message.from_user.id)

async def send_job(user_id: int):
    data = user_data[user_id]
    job = data["jobs"][data["index"]]

    text = (
        f"{job['title']}\n"
        f"Компанія: {job['company']}\n"
        f"Зарплата: {job['salary']}\n\n"
        f"{job['link']}\n\n"
        f"{data['index']+1}/{len(data['jobs'])}"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Наступна", callback_data="next")]
        ]
    )

    await bot.send_message(
        user_id,
        text,
        reply_markup=keyboard
    )

@dp.callback_query(lambda c: c.data == "next")
async def next_job(callback: CallbackQuery):
    user_id = callback.from_user.id
    data = user_data.get(user_id)

    if not data:
        await callback.answer("Сесія завершена")
        return

    data["index"] = (data["index"] + 1) % len(data["jobs"])
    job = data["jobs"][data["index"]]

    text = (
        f"{job['title']}\n"
        f"Компанія: {job['company']}\n"
        f"Зарплата: {job['salary']}\n\n"
        f"{job['link']}\n\n"
        f"{data['index']+1}/{len(data['jobs'])}"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Наступна", callback_data="next")]
        ]
    )

    await callback.message.edit_text(
        text,
        reply_markup=keyboard
    )

    await callback.answer()

async def main():
    print("Bot started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())