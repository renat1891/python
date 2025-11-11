import requests
from bs4 import BeautifulSoup
import json
import csv


link = "https://webscraper.io/test-sites/e-commerce/static/phones/touch"

response = requests.get(link)
soup = BeautifulSoup(response.text, 'lxml')

cards = soup.find_all('div', class_='card')
phones = []

for card in cards:
    title = card.find('a', class_='title').get_text(strip=True)
    price = card.find('h4', class_='price').get_text(strip=True)
    description = card.find('p', class_='description').get_text(strip=True)
    link_full = "https://webscraper.io" + card.find('a', class_='title')['href']
    
    reviews_tag = card.find('p', class_='pull-right')
    reviews = reviews_tag.get_text(strip=True) if reviews_tag else "Немає даних"

    phone = {
        "title": title,
        "price": price,
        "description": description,
        "reviews": reviews,
        "link": link_full
    }
    phones.append(phone)


with open("phones.json", "w", encoding="utf-8") as f:
    json.dump(phones, f, ensure_ascii=False, indent=4)


with open("phones.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "description", "reviews", "link"])
    writer.writeheader()
    writer.writerows(phones)

print(f"Знайдено товарів: {len(phones)}")
print("Дані збережено у файли: phones.json і phones.csv")



