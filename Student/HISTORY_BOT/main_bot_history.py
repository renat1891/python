import asyncio
import json
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from db import DB


TOKEN = "8460601382:AAG69xvejJIFFwlMZvRsWNniVOr5cM87hOM"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
db = DB()
id_channel = -1003823650090

def generate_question():
    history_data = db.get_history_data() 
    event = random.choice(list(history_data.keys()))
    correct = history_data[event]

    wrong = random.sample(
        [v for v in history_data.values() if v != correct], 3
    )

    options = wrong + [correct]
    random.shuffle(options)

    return event, correct, options

@dp.message(Command("start"))
async def start(message: types.Message):
    db.add_user(message.from_user.full_name, message.from_user.id)
    await message.answer("Я вітаю тебе в історичному боті! Використовуй /quiz щоб почати вікторину.")

@dp.message(Command("quiz"))
async def quiz(message: types.Message):
    await send()
    await message.answer("Вікторину надіслано в канал!")

async def send():
    history, correct, options = generate_question()

    find_correct_id = options.index(correct)
    await bot.send_poll(
        chat_id=id_channel,
        question=f"Яка подія {history} відбулася?",
        options=options,
        type="quiz",
        is_anonymous=True,
        correct_option_id=find_correct_id,
        explanation=f"Подія {history} є {correct}"
    )

async def time_send():
    while True:
        await send()
        await asyncio.sleep(10*60*60)  

async def main():
    print("Бот запущено")
    asyncio.create_task(time_send())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
