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
    if message.text.lower() == "1":
        await message.answer("January")
    elif message.text.lower() == "2":
        await message.answer("February")
    elif message.text.lower() == "3":
        await message.answer("March")
    elif message.text.lower() == "4":
        await message.answer("April")
    elif message.text.lower() == "5":
        await message.answer("May")
    elif message.text.lower() == "6":
        await message.answer("June")
    elif message.text.lower() == "7":
        await message.answer("July")
    elif message.text.lower() == "8":
        await message.answer("August")
    elif message.text.lower() == "9":
        await message.answer("September")
    elif message.text.lower() == "10":
        await message.answer("October")
    elif message.text.lower() == "11":
        await message.answer("November")
    elif message.text.lower() == "12":
        await message.answer("December")
    else:
        await message.answer("Please enter a number between 1 and 12.")

async def main():
    print("Starting bot...")
    await dp.start_polling(bot)
    print("Bot stopped.")

if __name__ == "__main__":
    asyncio.run(main())