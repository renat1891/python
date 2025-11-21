import requests
from bs4 import BeautifulSoup
import time


def send_telegram(title, price, link, image_url, time):
    TOKEN = "7756054942:AAHLVoZWAym72hYuebqTymYuPz8hgBkHd_U"
    chanel_id = "-1003275784278"

    text = f"{title}\n\n<span class=\"tg-spoiler\">{price}</span>\n\n<a href='{link}'>Посилання на оголошення</a>\n\n{time}"
    image_url = image_url.split(";")[0]
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={chanel_id}&photo={image_url}&caption={text}&parse_mode=HTML'

    response = requests.get(url)
    # print(response.json())

def get_olx_data(text):
    link = f"https://www.olx.ua/uk/list/q-{text}/?search%5Border%5D=created_at:desc"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "lxml")

    container = soup.find("div", class_="css-1sw7q4x") 
    if not container:
        return None

    items = soup.find_all("div", class_="css-1sw7q4x")
    for item in items:
        if "топ" in item.get_text(strip=True).lower():
            continue

        title_tag = item.find("h6") or item.find("h3") or item.find("h4")
        price_tag = item.find("p", class_="css-ol6ynp") or item.find("p", class_="css-blr5zl")
        time_tag = item.find("p", class_="css-1b24pxk").get_text(strip=True).split("-")[1]
        link_tag = item.find("a")
        image_tag = item.find("img")

        if not (title_tag and price_tag and link_tag and image_tag):
            continue

        return {
            "title": title_tag.get_text(strip=True),
            "price": price_tag.get_text(strip=True),
            "time": time_tag if time_tag else "не вказано",
            "link": "https://www.olx.ua" + link_tag["href"],
            "image": image_tag.get("src") or image_tag.get("data-src")
        }
    return None

search = input("Введіть пошуковий запит: ")
old_data = []
while True:
    data = get_olx_data(search)
    if data not in old_data:
        old_data.append(data)
    else:
        print("Оголошення не змінилося, чекаємо далі...")
        continue
    if data:
        send_telegram(data['title'], data['price'], data['link'], data['image'], data['time'])
    else:
        print("Оголошень не знайдено\n")
    time.sleep(1)