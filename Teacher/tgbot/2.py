import asyncio # асинхронна біліотека 
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token="7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U")
dp = Dispatcher()

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message()
async def cmd_start(message: types.Message):
    text = message.text.lower()
    if text in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
        month_number = int(text)
        if 1 <= month_number <= 12:
            await message.answer(months[month_number - 1])
        else:
            await message.answer("Please enter a number between 1 and 12.")
    else:
        await message.answer("Please enter a number between 1 and 12.")

async def main():
    print("Starting bot...")
    await dp.start_polling(bot)
    print("Bot stopped.")

if __name__ == "__main__":
    asyncio.run(main())


# 0
# > 12
# 12
# > -5
# 7


# > 10ms
# **km/h

# > 10kmh
# **m/s