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

regions = {
    "Волинська": "volynskaya",
    "Рівненська": "rivnenskaya",
    "Львівська": "lvovskaya",
    "Тернопільська": "ternopolskaya",
    "Хмельницька": "hmelitskaya",
    "Чернівецька": "chernovitskaya",
    "Івано-Франківська": "ivano-frankovskaya",
    "Київська": "kievskaya",
    "Одеська": "odesskaya",
    "Херсонська": "hersonskaya",
    "Дніпропетровська": "dnepropetrovskaya",
    "Донецька": "donetskaya",
    "Луганська": "luganskaya",
    "Сумська": "sumskaya",
    "Полтавська": "poltavskaya",
    "Житомирська": "zhitomirskaya",
    "Кіровоградська": "kirovogradskaya",
    "Вінницька": "vinnitskaya",
    "Чернігівська": "chernigovskaya",
    "Запорізька": "zaporozhskaya"
}

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
    if region not in regions:
        await message.answer("Будь ласка, виберіть регіон з клавіатури.")
        return
        
    fuels = get_data_info(category=regions.get(region).lower())

    if not fuels:
        await message.answer(f"На жаль, не вдалося отримати дані для {region}.")
        return
    text = f"__Ціни на пальне в {region}__\n\n"
    text += f"```{region}\n"

    text += f"|{'Тип':<19}|{'Ціна':<8}|{'Зміна':<8}|%\n"
    for fuel_type, data in fuels.items():
        text += f"|{fuel_type:<19}|{data['price']:<8}|{data['change']:<8}|{data['change_percent']}\n"

    await message.answer(text+"```", parse_mode="Markdown")

async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())