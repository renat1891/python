import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import random


bot = Bot(token="7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U")
dp = Dispatcher()

kb1 = [
    [types.KeyboardButton(text="Нова гра"), types.KeyboardButton(text="Здаюсь")],
]

keyboard = types.ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Я загадаю число і тобі треба буде його відгадати", reply_markup=keyboard)
    await gen_magic_num(message)

@dp.message(F.text.lower().strip() == "нова гра" or Command("new_game"))
async def gen_magic_num(message: types.Message):
    global magic_num
    await message.answer("нова гра почалась")
    magic_num = random.randint(1, 100)

@dp.message(F.text.lower() == "здаюсь")
async def guess(message: types.Message):
    await message.answer(f"Правильне число було {magic_num}")

@dp.message()
async def guess(message: types.Message):
    print("Received message:", message.text)
    text = message.text.lower()
    if not text.isdigit():
        await message.answer("Я вас не розумію")
        return
    guess_num = int(text)
    if guess_num<magic_num:
        await message.answer("число більше")
    elif guess_num>magic_num:
        await message.answer("число менше")
    else:
        await message.answer("ви вгадали число")



async def main():
    print("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
