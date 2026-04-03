      
    
from loguru import logger
import requests
import time
from parsing import sort_data

TOKEN = "8691711065:AAGkmrqN6NT_bBjX9bIq0S3mLsWae5kaxL8"
MONO_API  = "https://api.monobank.ua/bank/currency"
CHANNEL_ID = "-1003846107439"

def send_telegram(text):
    logger.info("Відправляю повідомлення в Telegram...")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    result = requests.get(url, data={
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "HTML"
    })
    logger.info(f"Повідомлення відправлено в Telegram: {result.text}")


def format_change(name, old_val, new_val):
    def line(label, old, new):
        if old is None or new == old:
            return None
        diff = round(new - old, 4)
        sign = "+" if diff > 0 else ""
        circle = "🟢" if diff > 0 else "🔴"
        return f"{label}: {new} ({sign}{diff}) {circle}"

    if type(new_val) is tuple:
        old_buy, old_sell = old_val if type(old_val) is tuple else (None, None)
        results = [
            line(f"{name} Купівля", old_buy, new_val[0]),
            line(f"{name} Продаж", old_sell, new_val[1]),
        ]
    else:
        results = [line(name, old_val, new_val)]

    return [r for r in results if r]


def check_and_notify(previous):
    logger.info("Перевіряю курси валют...")
    current = sort_data()

    changes = []
    for name, new_val in current.items():
        old_val = previous.get(name)

        if old_val is None:
            continue

        lines = format_change(name, old_val, new_val)
        changes.extend(lines)

    if changes:
        text = "<b>Зміни курсів валют</b>\n\n" + "\n".join(changes)
        send_telegram(text)
    else:
        logger.info("Курси не змінились, повідомлення не надсилається.")

    return current


def main():
    logger.info("Бот запущено. Перший збір курсів...")
    previous = sort_data()
    logger.info(f"Початкові курси збережено: {previous}")

    while True:
    
        time.sleep(3600)
        while True:    
            try:
                previous = check_and_notify(previous)
                break
            except ValueError as e:
                logger.warning(f"Помилка API (rate limit?), повторна спроба через 60 сек: {e}")
                time.sleep(60)


if __name__ == "__main__":
    main()