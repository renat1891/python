import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from parsing_workua.py import parse_python_jobs

TOKEN = "8534853373:AAE1sGuAR5ye4p5jDUIL6YT01gHFCE73168"

bot = Bot(TOKEN)
dp = Dispatcher()


user_jobs = {}

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Привіт \nНапиши місто (kyiv / lviv / remote), "
    )

@dp.message()
async def send_jobs(message: types.Message):
    city = message.text.lower().strip()
    jobs = parse_python_jobs(city, 10)

    if not jobs:
        await message.answer("Вакансій не знайдено")
        return

    user_jobs[message.from_user.id] = {"jobs": jobs, "index": 0}

    await send_job_message(message.from_user.id)

async def send_job_message(user_id: int):
    data = user_jobs[user_id]
    job = data["jobs"][data["index"]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton("Назва ", callback_data="title"),
            InlineKeyboardButton("Компанія ", callback_data="company"),
        ],
        [
            InlineKeyboardButton("Зарплата ", callback_data="salary"),
            InlineKeyboardButton("Посилання ", callback_data="link"),
        ],
        [
            InlineKeyboardButton("Наступна ", callback_data="next")
        ]
    ])

    text = f"Вакансія {data['index']+1}/{len(data['jobs'])}"
    await bot.send_message(user_id, text, reply_markup=keyboard)

@dp.callback_query()
async def handle_buttons(query: CallbackQuery):
    user_id = query.from_user.id
    data = user_jobs.get(user_id)
    if not data:
        await query.answer("Сесія закінчилась. Напиши місто знову.")
        return

    job = data["jobs"][data["index"]]

    if query.data == "next":
        data["index"] = (data["index"] + 1) % len(data["jobs"])
        await query.message.delete()
        await send_job_message(user_id)
    else:
        info = {
            "title": f"Назва: {job['title']}",
            "company": f" Компанія: {job['company']}",
            "salary": f" Зарплата: {job['salary']}",
            "link": f"Посилання: {job['link']}"
        }
        await query.answer(info[query.data], show_alert=True)

async def main():
    print("Bot started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())