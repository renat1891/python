import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from db import DB

TOKEN = "8323790629:AAHpR9W0bOVbJc89nnIIkgvYuCVUgdiauDU"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
db = DB()
id_channel = -1001234567890  

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Вітаю! Я бот з жартами. Використовуй /joke, щоб отримати жарт.")

@dp.message(Command("joke"))
async def joke(message: types.Message):
    jokes = db.get_all_jokes()
    if jokes:
        random_joke = random.choice(jokes)
        await message.answer(random_joke)
    else:
        await message.answer("На жаль, зараз немає жартів у базі даних.")

async def send_joke_to_channel():
    jokes = db.get_all_jokes()
    if jokes:
        random_joke = random.choice(jokes)
        await bot.send_message(chat_id=id_channel, text=random_joke)

async def scheduled_jokes():
    while True:
        current_hour = int(asyncio.get_event_loop().time() // 3600 % 24)
        print(current_hour)  
        if 9 <= current_hour <= 21:  
            await send_joke_to_channel()
        await asyncio.sleep(6 * 60 * 60)  

async def main():
    print("Бот запущено")
    asyncio.create_task(scheduled_jokes())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())