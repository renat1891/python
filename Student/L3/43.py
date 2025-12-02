import requests
import time

def send_telegram(price, drop, direction):
    TOKEN = "7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U"
    channel_id = "-1003275784278"

    binance_link = "https://www.binance.com/en/trade/ETH_USDT"

    emoji = "📉" if direction == "впав" else "📈"

    text = (
        f"{emoji} ETH {direction} на <b>${abs(drop)}</b>!\n\n"
        f"Поточна ціна: <b>${price}</b>\n\n"
        f"<a href='{binance_link}'>Посилання на Binance</a>"
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": channel_id,
        "text": text,
        "parse_mode": "HTML"
    })


def get_eth_price():
    try:
        r = requests.get(
            "https://api.binance.com/api/v3/ticker/price",
            params={"symbol": "ETHUSDT"},
            timeout=10
        )
        data = r.json()
        return int(float(data["price"]))
    except:
        return None


print("Старт моніторингу ETH з Binance...")

last_price = get_eth_price()
print(f"Початкова ціна ETH: ${last_price}")

THRESHOLD = 10

while True:
    time.sleep(10)

    price = get_eth_price()
    if price is None:
        continue

    diff = price - last_price

    if price % 10 == 0:
        if diff < 0:
            print(f"🔴 ETH: ${price} (−{abs(diff)})")
        elif diff > 0:
            print(f"🟢 ETH: ${price} (+{diff})")

    drop = last_price - price
    direction = "впав" if diff < 0 else "піднявся"

    if (price % 10 == 0) and (abs(drop) >= THRESHOLD):
        send_telegram(price, drop, direction)
        last_price = price

    if price > last_price:
        last_price = price
