import asyncio
import re
from itertools import cycle

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest

from openai import AsyncOpenAI



BOT_TOKEN = "7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



api_keys = {
    "github1": "f0af93f61ad44ceeb26a4aca6be8e75c",
    "github2": "74b0c0abd2294719ba29967c27bde367",
    "github3": "0710951b319a4cd79e155a8e40413658",
}

API_KEYS = list(api_keys.values())

AIMLAPI_BASE_URL = "https://api.aimlapi.com/v1"
MODEL_NAME = "openai/gpt-5-2"

key_cycle = cycle(API_KEYS)
key_lock = asyncio.Lock()


async def get_next_key():
    async with key_lock:
        return next(key_cycle)


_MD_V2_SPECIALS = r'[_*\[\]()~`>#+\-=|{}.!\\]'

def escape_markdown_v2(text: str) -> str:
    return re.sub(_MD_V2_SPECIALS, lambda m: "\\" + m.group(0), text)


async def gpt(text: str) -> str | None:
    last_error = None

    for _ in range(len(API_KEYS)):
        api_key = await get_next_key()

        client = AsyncOpenAI(
            base_url=AIMLAPI_BASE_URL,
            api_key=api_key,
        )

        try:
            response = await asyncio.wait_for(
                client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "Answer in Telegram MarkdownV2. "
                                "Keep formatting but ensure the text is valid MarkdownV2."
                            ),
                        },
                        {"role": "user", "content": text},
                    ],
                ),
                timeout=15,
            )

            return response.choices[0].message.content

        except Exception as e:
            last_error = e
            print(f"API key failed ({api_key[:6]}...): {e}")

    print("All API keys failed:", last_error)
    return None



@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Я GPT-5 бот\n"
        "Напиши повідомлення — я відповім"
    )


@dp.message()
async def handle_message(message: types.Message):
    if not message.text:
        return

    await message.answer("Думаю...")

    result = await gpt(message.text)

    if not result:
        await message.answer("Зараз не можу відповісти.")
        return

    
    try:
        await message.answer(
            result,
            parse_mode="MarkdownV2",
            disable_web_page_preview=True,
        )
        return
    except TelegramBadRequest:
        pass

    await message.answer(
        escape_markdown_v2(result),
        parse_mode="MarkdownV2",
        disable_web_page_preview=True,
    )

async def main():
    print(" Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())