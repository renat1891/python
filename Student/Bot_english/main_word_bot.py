import asyncio
import json
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import sqlite3

TOKEN = "8419752850:AAHDVFEU2prEH7YYbQG_Ob4I5npJue4qg-0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "A0.json")

with open(json_path, "r", encoding="utf-8") as f:
    WORDS = json.load(f)

def db():
    return sqlite3.connect("bot.db")

def initialize_db():
    conn = db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER UNIQUE,
            name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def update_db_structure():
    conn = db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id FROM user LIMIT 1")
    except sqlite3.OperationalError:
        cur.execute("ALTER TABLE user ADD COLUMN id INTEGER PRIMARY KEY AUTOINCREMENT")
        conn.commit()
    conn.close()

def initialize_user_word_table():
    conn = db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_word (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            word TEXT,
            correct_count INTEGER DEFAULT 0,
            incorrect_count INTEGER DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES user(id)
        )
    ''')
    conn.commit()
    conn.close()

def update_user_word_table():
    conn = db()
    cur = conn.cursor()
    try:
        cur.execute("SELECT status FROM user_word LIMIT 1")
    except sqlite3.OperationalError:
        cur.execute("ALTER TABLE user_word ADD COLUMN status TEXT DEFAULT 'unknown'")
        conn.commit()
    conn.close()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Вчити слова"), KeyboardButton(text="Статистика")]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Привіт\nОбирай дію:",
        reply_markup=keyboard
    )

@dp.message()
async def text_router(message: types.Message):
    if message.text == "Вчити слова":
        await learn(message)
    elif message.text == "Статистика":
        await stats(message)

async def learn(message: types.Message):
    tg_id = message.from_user.id
    conn = db()
    cur = conn.cursor()

    cur.execute("INSERT OR IGNORE INTO user (tg_id) VALUES (?)", (tg_id,))
    conn.commit()

    cur.execute("SELECT id FROM user WHERE tg_id=?", (tg_id,))
    user_id = cur.fetchone()[0]

    word = random.choice(list(WORDS.keys()))

    cur.execute(
        "INSERT OR IGNORE INTO user_word (user_id, word) VALUES (?,?)",
        (user_id, word)
    )
    conn.commit()

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Знаю", callback_data=f"1:{word}"),
                InlineKeyboardButton(text="Не знаю", callback_data=f"0:{word}")
            ]
        ]
    )

    await message.answer(f"{word}", reply_markup=keyboard)
    conn.close()

@dp.callback_query()
async def buttons(query: types.CallbackQuery):
    await query.answer()
    status, word = query.data.split(":")
    tg_id = query.from_user.id

    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM user WHERE tg_id=?", (tg_id,))
    user_id = cur.fetchone()[0]

    if status == "1":
        cur.execute(
            "UPDATE user_word SET status=1 WHERE user_id=? AND word=?",
            (user_id, word)
        )
        text = f"`{word}` більше не повториться"
    else:
        text = f"`{word}` ще буде повторюватись"

    conn.commit()
    conn.close()

    await query.message.edit_text(text + f"\n\n{WORDS[word]}", parse_mode="Markdown")

async def stats(message: types.Message):
    tg_id = message.from_user.id
    conn = db()
    cur = conn.cursor()

    cur.execute("""
    SELECT COUNT(*), SUM(status)
    FROM user_word
    JOIN user ON user.id = user_word.user_id
    WHERE user.tg_id=?
    """, (tg_id,))

    total, known = cur.fetchone()
    known = known or 0

    await message.answer(
        f"Статистика:\n"
        f"Всього слів: {total}\n"
        f"Знаю: {known}\n"
        f"Вчу: {total - known}"
    )
    conn.close()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    initialize_db()
    update_db_structure()
    initialize_user_word_table()
    update_user_word_table()
    asyncio.run(main())
