import asyncio # асинхронна біліотека 

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token="7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    print(message.from_user)
    await message.answer("Hello!")

@dp.message(Command("help"))
async def cmd_start(message: types.Message):
    await message.answer("bot will help you")

async def main():
    print("Starting bot...")
    await dp.start_polling(bot)
    print("Bot stopped.")

if __name__ == "__main__":
    asyncio.run(main())