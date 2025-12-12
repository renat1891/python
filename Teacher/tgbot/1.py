import asyncio # асинхронна біліотека 

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

import random

bot = Bot(token="7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U")
dp = Dispatcher()

facts = [
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "Bananas are berries, but strawberries aren't.",
    "Honey never spoils.",
    "A group of flamingos is called a 'flamboyance'.",
    "Octopuses have three hearts.",
    "There are more stars in the universe than grains of sand on all the world's beaches.",
    "Wombat poop is cube-shaped.",
    "The shortest war in history lasted 38 minutes.",
    "A day on Venus is longer than a year on Venus.",
    "Some cats are allergic to humans."
]

kb1 = [
    [types.KeyboardButton(text="Hello"), types.KeyboardButton(text="Bye")],
    [types.KeyboardButton(text="How are you?"), types.KeyboardButton(text="What's your name?")],
    [types.KeyboardButton(text="/fact")]
]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb1, resize_keyboard=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    print(message.from_user)
    await message.answer("Hello!", reply_markup=keyboard)

@dp.message(Command("fact"))
async def cmd_start(message: types.Message):
    await message.answer(random.choice(facts))

@dp.message()
async def cmd_start(message: types.Message):
    if message.text.lower() == "hello":
        await message.answer("Hello!")
    elif message.text.lower() == "bye":
        await message.answer("Goodbye!")
    elif message.text.lower() == "how are you?":
        await message.answer("I'm a bot, I don't have feelings, but thanks for asking!")
    elif message.text.lower() == "what's your name?":
        await message.answer("I'm your friendly Telegram bot!")
    else:
        await message.answer("I don't understand. Please ask me something else.")

async def main():
    print("Starting bot...")
    await dp.start_polling(bot)
    print("Bot stopped.")

if __name__ == "__main__":
    asyncio.run(main())