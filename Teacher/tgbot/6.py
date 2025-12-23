import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from openai import AsyncOpenAI


BOT_TOKEN = "7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U"

API_KEYS = {
    "github1": "f0af93f61ad44ceeb26a4aca6be8e75c",
    "github2": "74b0c0abd2294719ba29967c27bde367",
    "github3": "0710951b319a4cd79e155a8e40413658",
}

client = AsyncOpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key=API_KEYS["github3"],  
)

MODEL = "openai/gpt-5-2"  

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

user_tests = {}

async def gpt(messages):
    response = await client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    return response.choices[0].message.content


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "English Level Test Bot\n"
        "Напиши /test щоб пройти тест"
    )


@dp.message(Command("test"))
async def start_test(message: types.Message):
    await message.answer("Створюю тест...")

    prompt = """
Create an English level test with:
- 10 multiple-choice questions
- Grammar + vocabulary
- Each question has options A, B, C, D
- At the end, provide ONLY the questions
Do NOT provide answers yet.
"""

    test = await gpt([
        {"role": "system", "content": "You are an English teacher."},
        {"role": "user", "content": prompt},
    ])

    user_tests[message.from_user.id] = test

    await message.answer(
        " English Test\n\n"
        f"{test}\n\n"
        " Напиши відповіді одним рядком.\n"
        "Наприклад: A B C D A B C D A B"
    )


@dp.message()
async def check_answers(message: types.Message):
    user_id = message.from_user.id

    if user_id not in user_tests:
        return

    answers = message.text.strip()

    await message.answer(" Перевіряю відповіді...")

    prompt = f"""
Here is the test:
{user_tests[user_id]}

User answers:
{answers}

Check the test.
Count correct answers.
Determine English level:
0–2 = A1
3–4 = A2
5–6 = B1
7–8 = B2
9–10 = C1

Respond with:
- Score
- Level
- Short explanation
"""

    result = await gpt([
        {"role": "system", "content": "You are an English examiner."},
        {"role": "user", "content": prompt},
    ])

    del user_tests[user_id]

    await message.answer(
        "RESULT\n\n" + result
    )



async def main():
    print("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
