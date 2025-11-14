import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://www.olx.ua"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def parse_page(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    items = soup.select("div.css-1sw7q4x") 

    data = []
    for item in items:
        title = item.select_one("h4").get_text(strip=True) if item.select_one("h4") else None
        price = item.select_one("p[data-testid='ad-price']").get_text(strip=True) if item.select_one("p[data-testid='ad-price']") else None
        link_tag = item.select_one("a")
        link = BASE_URL + link_tag["href"] if link_tag else None

        data.append({
            "title": title,
            "price": price,
            "link": link
        })

    next_btn = soup.select_one("a[data-testid='pagination-forward']")
    next_url = BASE_URL + next_btn["href"] if next_btn else None

    return data, next_url

query = input("Введіть ваш пошуковий запит для OLX: ").strip()
url_query = query.replace(" ", "-")
URL = f"{BASE_URL}/uk/list/q-{url_query}/"

all_results = []
next_page = URL

while next_page:
    print("Парсинг:", next_page)
    data, next_page = parse_page(next_page)
    all_results.extend(data)

    time.sleep(1) 

print("\nЗнайдено оголошень:", len(all_results))

for x in all_results[:10]:
    print(x)
