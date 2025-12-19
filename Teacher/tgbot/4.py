import asyncio
import re
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest  # NEW
from openai import OpenAI, AsyncOpenAI


bot = Bot(token="7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U")
dp = Dispatcher()

_MD_V2_SPECIALS = r'[_*\[\]()~`>#+\-=|{}.!\\]'

def escape_markdown_v2(text: str) -> str:
    # Escape all Telegram MarkdownV2 special chars (including '.' and '\')
    return re.sub(_MD_V2_SPECIALS, lambda m: "\\" + m.group(0), text)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Я gpt-5 і можу відповідати на ваші запитання.")


async def gpt(text):  # Fixed async function definition
    api_keys = {
        "github1": "f0af93f61ad44ceeb26a4aca6be8e75c",
        "github2": "74b0c0abd2294719ba29967c27bde367",
        "github3": "0710951b319a4cd79e155a8e40413658",
    }

    AIMLAPI_BASE_URL = "https://api.aimlapi.com/v1"

    client = AsyncOpenAI(
        base_url=AIMLAPI_BASE_URL,
        api_key=api_keys["github3"],
    )

    response = await asyncio.wait_for(
        client.chat.completions.create(
            model="openai/gpt-5-2",
            messages=[
                {
                    "role": "system",
                    "content": "Answer in Telegram MarkdownV2. Keep formatting but ensure the text is valid MarkdownV2.",
                },
                {"role": "user", "content": text},
            ],
        ),
        timeout=15
    )
    print(response)  # Added print to display the response
    return response.choices[0].message.content

@dp.message()
async def guess(message: types.Message):
    text = message.text.lower()
    await message.answer("Думаю...")
    result = await gpt(text)

    if not result:
        await message.answer("Вибачте, я не можу відповісти на це зараз.")
        return

    # 1) Try send as real MarkdownV2 (preserves formatting)
    try:
        await message.answer(
            result,
            disable_web_page_preview=True,
            parse_mode="MarkdownV2",
        )
        return
    except TelegramBadRequest:
        pass

    # 2) Fallback: escape everything (no formatting, but never crashes)
    escaped_result = escape_markdown_v2(result)
    await message.answer(
        escaped_result,
        disable_web_page_preview=True,
        parse_mode="MarkdownV2",
    )

async def main():
    print("Bot started!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
