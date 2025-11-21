import requests
from bs4 import BeautifulSoup
import time


def send_telegram(title, price, link, image_url):
    TOKEN = "756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U"
    chanel_id = "-1003275784278"

    text = f"{title}\n\n<span class=\"tg-spoiler\">{price}</span>\n\n<a href='{link}'>Посилання на авто</a>"
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    requests.post(url, data={
        "chat_id": chanel_id,
        "caption": text,
        "parse_mode": "HTML",
        "photo": image_url
    })


def get_autoria_list(query):
    link = f"https://auto.ria.com/uk/search/?category_id=1&keywords={query}&order_by=dates.created.desc"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    items = soup.find_all("section", class_="ticket-item")
    results = []

    for item in items:
        title_tag = item.find("a", class_="address")
        price_tag = item.find("span", class_="bold size22")
        link_tag = item.find("a", class_="address")
        image_tag = item.find("img")

        if not (title_tag and price_tag and link_tag and image_tag):
            continue

        title = title_tag.get_text(strip=True)
        price = price_tag.get_text(strip=True)
        link = link_tag["href"]
        image = image_tag.get("src") or image_tag.get("data-src")

        results.append({
            "title": title,
            "price": price,
            "link": link,
            "image": image
        })

    return results


search = input("Введіть пошуковий запит: ")
sent_cars = set()

while True:
    cars = get_autoria_list(search)

    if not cars:
        print("Оголошень не знайдено")
        time.sleep(3)
        continue

    for car in cars:
        car_id = car["link"]

        if car_id not in sent_cars:
            send_telegram(car['title'], car['price'], car['link'], car['image'])
            print(f"Відправлено: {car['title']}")
            sent_cars.add(car_id)
        else:
            print("Вже відправлялось:", car["title"])

    time.sleep(3)

