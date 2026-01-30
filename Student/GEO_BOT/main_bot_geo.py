import asyncio
import json
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from db import DB

TOKEN = "8234958188:AAH2Z3hKExaMOgTI8BbDWp_9UC7mdP-loIo"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
db = DB()

id_channel = -1003823650090

def generate_question():
    countries_data = db.get_countries_data() 
    country = random.choice(list(countries_data.keys()))
    correct = countries_data[country]

    wrong = random.sample(
        [v for v in countries_data.values() if v != correct], 3
    )

    options = wrong + [correct]
    random.shuffle(options)

    return country, correct, options

@dp.message(Command("start"))
async def start(message: types.Message):
    db.add_user(message.from_user.full_name, message.from_user.id)
    await message.answer("Я вітаю тебе в географічному боті! Використовуй /quiz щоб почати вікторину.")

@dp.message(Command("quiz"))
async def quiz(message: types.Message):
    country, correct, options = generate_question()

    find_correct_id = options.index(correct)
    await bot.send_poll(
        chat_id=id_channel,
        question=f"Яка столиця {country}",
        options=options,
        type="quiz",
        is_anonymous=True,
        correct_option_id=find_correct_id,
        explanation=f"Столиця {country} є {correct}"
    )
    await message.answer("Вікторину надіслано в канал!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
