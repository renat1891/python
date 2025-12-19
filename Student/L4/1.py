import asyncio
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

bot = Bot(token="7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U")
dp = Dispatcher()

words = ["python", "school", "telegram", "bot", "game"]

secret_word = ""
progress = []
attempts = 0

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[[types.KeyboardButton(text="Нова гра")]],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("вгадай слово")
   

@dp.message(Command("word"))
async def start_word_game(message: types.Message):
    await new_game(message)

@dp.message(F.text.lower() == "нова гра")
async def new_game(message: types.Message):
    global secret_word, progress, attempts

    secret_word = random.choice(words)
    progress = ["_"] * len(secret_word)
    attempts = 6

    await message.answer(f"Я загадав слово\n", f"{' '.join(progress)}\n", f"Спроб: {attempts}",reply_markup=keyboard)
        
@dp.message()
async def guess_letter(message: types.Message):
    global attempts, progress

    if message.text.startswith("/"):
        return

    if not secret_word:
        return

    letter = message.text.lower()

    if len(letter) != 1 or not letter.isalpha():
        await message.answer("Введи тільки одну літеру")
        return

    if letter in secret_word:
        for i, ch in enumerate(secret_word):
            if ch == letter:
                progress[i] = letter
    else:
        attempts -= 1

    if "_" not in progress:
        await message.answer(f"Ти вгадав: {secret_word}")
        return

    if attempts == 0:
        await message.answer(f"Ти програв. Слово було: {secret_word}")
        return

    await message.answer(
        f"{' '.join(progress)}\n"
        f"Спроб: {attempts}"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
