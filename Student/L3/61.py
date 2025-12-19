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

magic_num = None 

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Я загадаю число і тобі треба буде його відгадати", reply_markup=keyboard)
    await gen_magic_num(message)

@dp.message(lambda message: (message.text and message.text.lower() == "нова гра") 
                             or (message.text and message.text.startswith("/new_game")))
async def new_game(message: types.Message):
    await gen_magic_num(message)

async def gen_magic_num(message: types.Message):
    global magic_num
    magic_num = random.randint(1, 100)
    await message.answer("Нова гра почалась")

@dp.message(F.text.lower() == "здаюсь")
async def give_up(message: types.Message):
    global magic_num
    await message.answer(f"Правильне число було {magic_num}")

@dp.message()
async def guess(message: types.Message):
    global magic_num
    text = message.text.lower()
    if not text.isdigit():
        await message.answer("Я вас не розумію")
        return
    guess_num = int(text)
    if guess_num < magic_num:
        await message.answer("Число більше")
    elif guess_num > magic_num:
        await message.answer("Число менше")
    else:
        await message.answer("Ви вгадали число")

async def main():
    print("Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
