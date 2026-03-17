# напиги бота до парсингу
import asyncio
from datetime import datetime, timedelta
import aiohttp

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from parsing_fuel_bot import get_data_info
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


TOKEN = "8451436590:AAGdBZfo-3XRmnmNv87OBEpdq79dGxbsVd8"

bot = Bot(token=TOKEN)
dp = Dispatcher()





region_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Волинська")],
        [KeyboardButton(text="Рівненська")],
        [KeyboardButton(text="Львівська")],
        [KeyboardButton(text="Тернопільська")],
        [KeyboardButton(text="Хмельницька")],
        [KeyboardButton(text="Чернівецька")],
        [KeyboardButton(text="Івано-Франківська")],
        [KeyboardButton(text="Київська")],
        [KeyboardButton(text="Одеська")],
        [KeyboardButton(text="Херсонська")],
        [KeyboardButton(text="Дніпропетровська")],
        [KeyboardButton(text="Донецька")],
        [KeyboardButton(text="Луганська")],
        [KeyboardButton(text="Сумська")],
        [KeyboardButton(text="Полтавська")],
        [KeyboardButton(text="Житомирська")],
        [KeyboardButton(text="Кіровоградська")],
        [KeyboardButton(text="Вінницька")],
        [KeyboardButton(text="Чернігівська")],
        [KeyboardButton(text="Запорізька")],
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(
        "Привіт\nОберіть категорію пального:",
        reply_markup=region_keyboard
    )



@dp.message()
async def handle_region(message: types.Message):
    region = message.text
    fuels = get_data_info(category=region.lower())

    if not fuels:
        await message.answer(f"На жаль, не вдалося отримати дані для {region}.")
        return

    text = f"Ціни на пальне в {region}:\n\n"
    text += "Тип       Ціна    Зміна   %\n"
    text += "-----------------------------\n"

    for fuel_type, data in fuels.items():
        text += f"{fuel_type:<10}{data['price']:<8}{data['change']:<8}{data['change_percent']}\n"

    await message.answer(text)

async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())