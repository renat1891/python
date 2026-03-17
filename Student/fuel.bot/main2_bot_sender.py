import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime


def send_telegram(text):
    TOKEN = "8451436590:AAGdBZfo-3XRmnmNv87OBEpdq79dGxbsVd8"
    channel_id = "-1003846107439"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": channel_id,
        "text": text,
        "parse_mode": "HTML"
    })

def get_data_info(url="https://index.minfin.com.ua/ua/markets/fuel/reg/"):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    items = soup.select_one("table")
    rows = items.find_all("tr")[1:]
    fuels = {}
    for row in rows:
        cols = row.find_all("td")
        fuel_type = cols[0].text.strip()
        price = cols[1].text.strip()
        change = cols[2].text.strip()
        change_precent = cols[3].text.strip()
        fuels[fuel_type] = {"price": price, "change": change, "change_percent": change_precent}
    return fuels


def main():
    fuels = get_data_info()
    text = f"__Ціни на пальне в Україні__\n\n"
    text += f"```Україна\n"
    text += f"|{'Тип':<19}|{'Ціна':<8}|{'Зміна':<8}|%\n"
    for fuel_type, data in fuels.items():
        text += f"|{fuel_type:<19}|{data['price']:<8}|{data['change']:<8}|{data['change_percent']}\n"
    send_telegram(text+"```")


    

print("Скрипт запущено. Очікування потрібного часу...")

while True:
    now = datetime.now()
    if now.minute % 60 == 0 and now.second == 0:
        main()
        time.sleep(60)  
    else:
        time.sleep(1) 
        print(now)

