import asyncio
import json
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from db import DB
TOKEN = "8419752850:AAHDVFEU2prEH7YYbQG_Ob4I5npJue4qg-0"

bot = Bot(token=TOKEN)
dp = Dispatcher()
db=DB()
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вчити слова"),
            KeyboardButton(text="Мій прогреcс")
        ],
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Hello! I'm your English learning bot.")
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    if not db.get_user(user_id):
        db.add_user(user_name, user_id)
        db.add_words_for_user(user_id)
        await message.answer("You have been registered and words have been added to your account.", reply_markup=keyboard)
    else:
        await message.answer("You are already registered.", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Вчити слова")
async def learn_words(message: types.Message):
    user_id = message.from_user.id
    word_data = db.get_random_word(user_id)
    if word_data:
        word_id, word, translation, status = word_data
        buttons = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Знаю", callback_data=f"know_{word_id}"),
                InlineKeyboardButton(text="Не знаю", callback_data=f"dontknow_{word_id}")
            ]
        ])
        await message.answer(f"Слово: {word}\nПереклад: ||{translation}||", reply_markup=buttons, parse_mode="MarkdownV2")
    else:
        await message.answer("Ви вивчили всі слова!")

@dp.callback_query(lambda c: c.data and c.data.startswith(("know_", "dontknow_")))
async def process_word_response(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data

    # Логування callback_data для діагностики
    print(f"Received callback data: {data}")

    try:
        action, word_id = data.split("_")
        word_id = int(word_id)
    except ValueError as e:
        await callback_query.answer("Неправильний формат даних.", show_alert=True)
        print("Error: Invalid callback data format.", e)
        return

    if action == "know":
        db.update_word_status(user_id, word_id, 1)
    elif action == "dontknow":
        db.update_word_status(user_id, word_id, 0)

    await callback_query.answer()
    
    # Дістаньте наступне слово
    word_data = db.get_random_word(user_id)
    if word_data:
        word_id, word, translation, status = word_data
        buttons = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Знаю", callback_data=f"know_{word_id}"),
                InlineKeyboardButton(text="Не знаю", callback_data=f"dontknow_{word_id}")
            ]
        ])
        await callback_query.message.edit_text(f"Слово: {word}\nПереклад: ||{translation}||", reply_markup=buttons, parse_mode="MarkdownV2")
    else:
        await callback_query.message.edit_text("Ви вивчили всі слова!")

@dp.message(lambda message: message.text == "Мій прогреcс")
async def show_progress(message: types.Message):
    user_id = message.from_user.id
    user_stats = db.stats_user(user_id)
    await message.answer("Ваш прогрес: ...")
    if user_stats:
        learned_count, total_count = user_stats
        await message.answer(f"Ви вивчили {learned_count} з {total_count} слів.")
    else:
        await message.answer("Не вдалося отримати ваш прогрес.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

