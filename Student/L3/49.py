import requests
import time


def send_telegram(text):
    TOKEN = "PUT_NEW_TOKEN_HERE"
    channel_id = "-1003275784278"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": channel_id, "text": text})


def get_btc_price_binance():
    try:
        r = requests.get(
            "https://api.binance.com/api/v3/ticker/price",
            params={"symbol": "BTCUSDT"},
            timeout=10
        )
        return float(r.json()["price"])
    except:
        return None

def round_to(price, n=100):
    return round(price/n) *n

print("Старт моніторингу BTC...")

price = get_btc_price_binance()
if price is None:
    print("Помилка отримання ціни")
    exit()

round_price = 10

level = round_to(price, round_price)
print(f"Початкова ціна: {price} → рівень: {level}")

while True:
    time.sleep(3)


    price = get_btc_price_binance()
    if price is None:
        continue

    if price >= level + round_price:
        new_level = round_to(price, round_price)
        send_telegram(f"🟢 BTC піднявся → {new_level}")
        level = new_level
    elif price <= level - round_price:
        new_level = round_to(price, round_price)
        send_telegram(f"🔴 BTC впав → {new_level}")
        level = new_level

    print(f"BTC: {price} | рівень: {level}")
