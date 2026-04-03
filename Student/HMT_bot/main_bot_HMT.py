
import json
import random
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

API_TOKEN = "8712577024:AAHKgAozJiu-Gg8nkNxddWMpBo8BHuED1M8"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

current_dir = os.path.dirname(__file__)


SUBJECTS = {
    "Математика":    os.path.join(current_dir, "math.json"),
    "Українська мова": os.path.join(current_dir, "ukrainian.json"),
    "Історія":       os.path.join(current_dir, "history.json"),
    "Фізика":        os.path.join(current_dir, "physics.json"),
}

subject_data = {}
for name, path in SUBJECTS.items():
    with open(path, "r", encoding="utf-8") as f:
        subject_data[name] = json.load(f)


TOTAL_QUESTIONS = 10
MIN_SCORE = 0
MAX_SCORE = 200

def calculate_nmt_score(correct: int) -> int:
    """Конвертує кількість правильних відповідей у бали НМТ (100–200)"""
    return round(MIN_SCORE + (correct / TOTAL_QUESTIONS) * (MAX_SCORE - MIN_SCORE))

def get_grade(score: int) -> str:
    """Повертає оцінку на основі балу"""
    if score >= 190:
        return "Відмінно"
    elif score >= 175:
        return "Добре"
    elif score >= 150:
        return "Задовільно"
    elif score >= 125:
        return "Слабко"
    else:
        return "Незадовільно"

def subjects_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=name)] for name in SUBJECTS],
        resize_keyboard=True
    )

user_state = {}


@dp.message()
async def message_handler(message: types.Message):
    text = message.text

    if text == "/start":
        await message.answer(
            "Це тренажер у форматі НМТ.\n\n"
            "Обери предмет для тесту:",
            reply_markup=subjects_keyboard()
        )
        return

    if text in SUBJECTS:
        user_id = message.from_user.id
        data = subject_data[text]

        all_questions = []
        for topic in data["topics"]:
            all_questions.extend(topic["questions"])

        questions = random.sample(all_questions, k=min(TOTAL_QUESTIONS, len(all_questions)))

        user_state[user_id] = {
            "subject": text,
            "questions": questions,
            "current": 0,
            "score": 0
        }

        await message.answer(
            f"Тест з предмету: {text}\n"
            f"Кількість питань: {len(questions)}\n"
            f"Шкала оцінювання: 100–200 балів (НМТ)\n\n"
            "Починаємо"
        )
        await send_quiz(message.chat.id, user_id)
        return

@dp.poll_answer()
async def poll_answer_handler(poll_answer: types.PollAnswer):
    user_id = poll_answer.user.id

    if user_id not in user_state:
        return

    data = user_state[user_id]
    q = data["questions"][data["current"]]

    correct_index = q["options"].index(q["correct_answer"])
    chosen_index = poll_answer.option_ids[0]

    if chosen_index == correct_index:
        data["score"] += 1

    data["current"] += 1

    if data["current"] < len(data["questions"]):
        await send_quiz(poll_answer.user.id, user_id)
    else:
        correct = data["score"]
        total = len(data["questions"])
        nmt_score = calculate_nmt_score(correct)
        grade = get_grade(nmt_score)


        await bot.send_message(
            poll_answer.user.id,
            f"Тест завершено!\n\n"
            f"Предмет: {data['subject']}\n"
            f"Правильних відповідей: {correct}/{total}\n"
            f"Бал НМТ: {nmt_score} / 200\n"
            f"{grade}\n\n"
            f"Обери предмет для наступного тесту:",
            reply_markup=subjects_keyboard()
        )
        del user_state[user_id]

async def send_quiz(chat_id: int, user_id: int):
    data = user_state[user_id]
    q = data["questions"][data["current"]]
    total = len(data["questions"])

    correct_index = q["options"].index(q["correct_answer"])

    await bot.send_poll(
        chat_id=chat_id,
        question=f"[{data['current'] + 1}/{total}] {q['question']}",
        options=q["options"],
        type="quiz",
        correct_option_id=correct_index,
        explanation=q.get("explanation", ""),
        is_anonymous=False,
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())