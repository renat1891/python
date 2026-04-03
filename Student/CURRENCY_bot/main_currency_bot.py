
import asyncio
import aiohttp
from datetime import datetime


from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = "8691711065:AAGkmrqN6NT_bBjX9bIq0S3mLsWae5kaxL8"
MONO_API  = "https://api.monobank.ua/bank/currency"
CHECK_INTERVAL = 60

bot = Bot(token=API_TOKEN)
dp  = Dispatcher()

CURRENCIES = {
    840: ("USD", "🇺🇸"),
    978: ("EUR", "🇪🇺"),
    826: ("GBP", "🇬🇧"),
    756: ("CHF", "🇨🇭"),
    985: ("PLN", "🇵🇱"),
}

last_dates: dict[int, int] = {}

last_rates: dict[int, tuple[float, float]] = {}

subscribers: set[int] = set()


async def get_raw_rates() -> list[dict] | None:
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(MONO_API) as r:
                data = await r.json(content_type=None)

        if not isinstance(data, list):
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Неочікувана відповідь API: {data}")
            return None

        return [item for item in data if isinstance(item, dict)]

    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Помилка запиту: {e}")
        return None


def format_rates(data: list[dict]) -> str:
    now   = datetime.now().strftime("%d.%m.%Y %H:%M")
    lines = [f"<b>Курси валют</b> | {now}\n"]

    for item in data:
        code_a = item.get("currencyCodeA")
        code_b = item.get("currencyCodeB")

        if code_b != 980 or code_a not in CURRENCIES:
            continue

        abbr, flag = CURRENCIES[code_a]
        buy  = item.get("rateBuy")
        sell = item.get("rateSell")

        if not buy or not sell:
            continue

        prev = last_rates.get(code_a)

        
        if prev:
            prev_buy, prev_sell = prev
            diff_buy  = buy - prev_buy
            diff_sell = sell - prev_sell

            lines.append(
                f"{flag} {abbr}: "
                f"куп <b>{buy:.2f}</b> ({diff_buy:+.2f}) ₴ | "
                f"прод <b>{sell:.2f}</b> ({diff_sell:+.2f}) ₴"
            )
        else:
            lines.append(
                f"{flag} {abbr}: "
                f"куп <b>{buy:.2f}</b> ₴ | "
                f"прод <b>{sell:.2f}</b> ₴"
            )

    return "\n".join(lines)


async def monitor_rates():
    while True:
        data = await get_raw_rates()

        if data:
            updated = []

            for item in data:
                code_a = item.get("currencyCodeA")
                code_b = item.get("currencyCodeB")

                if code_b != 980 or code_a not in CURRENCIES:
                    continue

                buy  = item.get("rateBuy")
                sell = item.get("rateSell")

                if not buy or not sell:
                    continue

                prev = last_rates.get(code_a)

                if prev:
                    prev_buy, prev_sell = prev
                    diff_buy  = buy - prev_buy
                    diff_sell = sell - prev_sell

                    
                    if diff_buy != 0 or diff_sell != 0:
                        abbr, flag = CURRENCIES[code_a]

                        updated.append(
                            f"{flag} {abbr}: "
                            f"куп {buy:.2f} ({diff_buy:+.2f}) | "
                            f"прод {sell:.2f} ({diff_sell:+.2f})"
                        )

                last_rates[code_a] = (buy, sell)

            if updated and subscribers:
                text = "<b>Зміни курсів:</b>\n\n" + "\n".join(updated)

                for uid in list(subscribers):
                    try:
                        await bot.send_message(uid, text, parse_mode="HTML")
                    except Exception:
                        subscribers.discard(uid)

        await asyncio.sleep(CHECK_INTERVAL)


kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Курси"), KeyboardButton(text="Підписатись")],
        [KeyboardButton(text="Відписатись")],
    ],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Бот курсу валют від Monobank\n"
        "Сповіщу коли курс зміниться",
        reply_markup=kb
    )


@dp.message(F.text == "💱 Курси")
async def cmd_rates(message: types.Message):
    data = await get_raw_rates()

    if data is None:
        await message.answer("Не вдалось отримати курси.")
        return

    await message.answer(format_rates(data), parse_mode="HTML")


@dp.message(F.text == "Підписатись")
async def cmd_subscribe(message: types.Message):
    subscribers.add(message.from_user.id)
    await message.answer("Підписано!")


@dp.message(F.text == "Відписатись")
async def cmd_unsubscribe(message: types.Message):
    subscribers.discard(message.from_user.id)
    await message.answer("Відписано.")


async def main():
    asyncio.create_task(monitor_rates())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())