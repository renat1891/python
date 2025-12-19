import asyncio
import random
import string
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

bot = Bot(token="7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U")
dp = Dispatcher()

main_kb = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="Пароль"), types.KeyboardButton(text="Нік")],
        [types.KeyboardButton(text="Випадкове число"), types.KeyboardButton(text="Кинути кубик")],
        [types.KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

password_kb = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="8 цифри+букви"), types.KeyboardButton(text="8 тільки букви")],
        [types.KeyboardButton(text="12 цифри+букви"), types.KeyboardButton(text="12 тільки букви")],
        [types.KeyboardButton(text="16 цифри+букви"), types.KeyboardButton(text="16 тільки букви")],
        [types.KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Використовуй /random для генерації",
        reply_markup=main_kb
    )

@dp.message(Command("random"))
async def random_menu(message: types.Message):
    await message.answer("Вибери опцію:", reply_markup=main_kb)

@dp.message()
async def handle_random(message: types.Message):
    text = message.text.strip()

    if text == "Пароль":
        await message.answer("Оберіть параметри пароля:", reply_markup=password_kb)
        return

    if text in ["8 цифри+букви", "12 цифри+букви", "16 цифри+букви"]:
        length = int(text.split()[0])
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for _ in range(length))
        await message.answer(f"Ваш пароль: `{password}`", parse_mode="Markdown", reply_markup=main_kb)
        return

    if text in ["8 тільки букви", "12 тільки букви", "16 тільки букви"]:
        length = int(text.split()[0])
        password = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        await message.answer(f"Ваш пароль: `{password}`", parse_mode="Markdown", reply_markup=main_kb)
        return

    if text == "Нік":
        nick = "User" + ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        await message.answer(f"Ваш нік: {nick}", reply_markup=main_kb)
        return

    if text == "Випадкове число":
        num = random.randint(1, 100)
        await message.answer(f"Випадкове число: {num}", reply_markup=main_kb)
        return

    if text == "Кинути кубик":
        dice = random.randint(1, 6)
        await message.answer(f"Випадок кубика: {dice}", reply_markup=main_kb)
        return

    if text == "Назад":
        await message.answer("Головне меню:", reply_markup=main_kb)
        return

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
