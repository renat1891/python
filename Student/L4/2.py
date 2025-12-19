import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

bot = Bot(token="7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U")
dp = Dispatcher()

habits = []        
adding = False     


menu_kb = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="Додати"), types.KeyboardButton(text="Зроблено")],
        [types.KeyboardButton(text="Статистика")],
        [types.KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

back_kb = types.ReplyKeyboardMarkup(
    keyboard=[[types.KeyboardButton(text="Назад")]],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Я трекер звичок",
        reply_markup=menu_kb
    )


@dp.message(Command("habits"))
async def habits_menu(message: types.Message):
    if not habits:
        text = "Твої звички:\n— поки немає"
    else:
        text = "Твої звички:\n"
        for i, (h, done) in enumerate(habits, start=1):
            text += f"{i}. {'+' if done else '-'} {h}\n"
    await message.answer(text, reply_markup=menu_kb)

@dp.message()
async def handle_text(message: types.Message):
    global adding, habits
    text = message.text.strip()

    if text == "Додати":
        adding = True
        await message.answer("Введи назву нової звички:", reply_markup=back_kb)
        return

    if text == "Статистика":
        done = sum(1 for _, d in habits if d)
        total = len(habits)
        await message.answer(f"Статистика за день: {done}/{total} виконано", reply_markup=menu_kb)
        return

    if text == "Зроблено":
        if not habits:
            await message.answer("Немає звичок")
            return
        msg = "Введи номер звички, яку виконав:\n"
        for i, (h, done) in enumerate(habits, start=1):
            msg += f"{i}. {'+' if done else '-'} {h}\n"
        await message.answer(msg)
        return

    if text == "Назад":
        await habits_menu(message)
        adding = False
        return

    if adding:
        habits.append((text, False))
        adding = False
        await message.answer(f"Звичку «{text}» додано", reply_markup=menu_kb)
        return

    if text.isdigit():
        idx = int(text) - 1
        if 0 <= idx < len(habits):
            name, _ = habits[idx]
            habits[idx] = (name, True)
            await message.answer(f"Звичку «{name}» відмічено", reply_markup=menu_kb)
        return

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
