import asyncio
import json
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8419752850:AAHDVFEU2prEH7YYbQG_Ob4I5npJue4qg-0"

bot = Bot(token=TOKEN)
dp = Dispatcher()





async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
