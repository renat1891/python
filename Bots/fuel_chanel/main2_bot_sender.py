from loguru import logger
import os
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import json


TOKEN = "8451436590:AAGdBZfo-3XRmnmNv87OBEpdq79dGxbsVd8"
CHANNEL_ID = "-1003846107439"

DATA_FILE = "last_data.json"


def send_telegram(text):
    logger.info("Відправляю повідомлення в Telegram...")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    result =requests.get(url, data={
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "HTML"
    })
    logger.info(f"Повідомлення відправлено в Telegram: {result.text}")


def get_data_info(url="https://index.minfin.com.ua/ua/markets/fuel/"):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    table = soup.select_one("table")
    rows = table.find_all("tr")[1:]

    fuels = {}

    for row in rows:
        cols = row.find_all("td")

        fuel_type = cols[0].text.strip()
        price = cols[2].text.strip()
        change = cols[3].text.strip()
        change_percent = cols[4].text.strip()

        fuels[fuel_type] = {
            "price": price,
            "change": change, 
            "change_percent": change_percent
        }

    return fuels


def load_last_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def save_last_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def format_message(fuels):
    text = "<b>Ціни на пальне в Україні</b>\n\n"
    text += "<pre>Україна\n"
    text += f"|{'Тип':<19}|{'Ціна':<8}|{'Зміна':<8}|%\n"

    for fuel_type, data in fuels.items():
        text += f"|{fuel_type:<19}|{data['price']:<8}|{data['change']:<8}|{data['change_percent']}\n"
    text += "</pre>"

    return text


def main():
    try:
        fuels = get_data_info()
        last_data = load_last_data()

        if fuels == last_data:
            print(f"[{datetime.now()}] Немає змін")
            return

        print(f"[{datetime.now()}] Є оновлення!")

        text = format_message(fuels)
        send_telegram(text)

        save_last_data(fuels)

    except Exception as e:
        print("Помилка:", e)


print("Скрипт запущено...")

while True:
    main()
    time.sleep(15)  