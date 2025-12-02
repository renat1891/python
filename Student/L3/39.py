import requests
import time
from bs4 import BeautifulSoup


def send_telegram(price, drop):
    print("send telegram")
    TOKEN = "7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U"
    channel_id = "-1003275784278"

    binance_link = "https://www.binance.com/en/trade/BTC_USDT"

    text = (
        f"📉 BTC впав на <b>${drop}</b>!\n\n"
        f"<span class=\"tg-spoiler\">Поточна ціна: ${price}</span>\n\n"
        f"<a href='{binance_link}'>Посилання на Binance</a>"
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={channel_id}&text={text}&parse_mode=HTML"

    response = requests.get(url)

    # print(response.json())


def get_btc_price_binance():
    try:
        r = requests.get(
            "https://api.binance.com/api/v3/ticker/price",
            params={"symbol": "BTCUSDT"},
            timeout=10
        )
        data = r.json()
        return int(float(data["price"]))
    except:
        return None


# def fetch_data_with_bs4(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#     }
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, "lxml")
#     return soup


# def parse_price(price_text):
#     price = "".join(filter(str.isdigit, price_text))  
#     return int(price) if price else 0


# def compare_prices(new_price, old_price):
#     difference = new_price - old_price
#     if difference >= THRESHOLD:
#         return "Ціна піднялася на 1000 або більше"
#     elif difference <= -THRESHOLD:
#         return "Ціна впала на 1000 або більше"
#     else:
#         return "Ціна змінилася менш ніж на 1000"


print("Старт моніторингу BTC з Binance...")

last_price = get_btc_price_binance()
print(f"Початкова ціна: ${last_price}")

THRESHOLD = 10 

while True:
    time.sleep(5)

    price = get_btc_price_binance()
    if price is None:
        continue

    drop = abs(last_price - price)
    print(f"BTC: ${price}")

    if drop >= THRESHOLD:
        print(f"Зміна курсу більше за {THRESHOLD}")
        send_telegram(price, drop)
        last_price = price





