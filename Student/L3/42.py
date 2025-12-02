import requests
import time

def send_telegram(text):
    TOKEN = "7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U"
    channel_id = "-1003275784278"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": channel_id,
        "text": text,
        "parse_mode": "HTML"
    })


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


print("Старт моніторингу BTC з Binance...")

last_price = get_btc_price_binance()
print(f"Початкова ціна: ${last_price}")

THRESHOLD = 100

while True:
    time.sleep(10)

    price = get_btc_price_binance()
    if price is None:
        continue
    print("BTC now: ", price)
    diff = price - last_price
    
    if abs(diff) > THRESHOLD:
        if diff < 0:
            text = f"🔴 BTC: ${price} (−{abs(diff)})"
            direction = "впав"
        elif diff > 0:
            text = f"🟢 BTC: ${price} (+{diff})"
            direction = "піднявся"
        print(text)
        send_telegram(text)
        last_price = price