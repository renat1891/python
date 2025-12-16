import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token="7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Введіть число з ms або kmh, і я його конвертую")


@dp.message()
async def convert(message: types.Message):
    text = message.text.lower().strip()

    if text.endswith("ms"):
        num = text[:-2].strip() 
        if not num.replace(".", "").isdigit():
            await message.answer("Я вас не розумію")
            return

        ms = float(num)
        kmh = ms * 3.6
        await message.answer(f"{ms} ms = {kmh:.2f} kmh")

    elif text.endswith("kmh"):
        num = text[:-3].strip() 
        if not num.replace(".", "").isdigit():
            await message.answer("Я вас не розумію")
            return

        kmh = float(num)
        ms = kmh / 3.6
        await message.answer(f"{kmh} kmh = {ms:.2f} ms")

    else:
        await message.answer("Я вас не розумію")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
