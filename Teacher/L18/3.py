import requests

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

    print(response.json())

send_telegram("10000", "100")