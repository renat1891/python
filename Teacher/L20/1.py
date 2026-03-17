import requests
from bs4 import BeautifulSoup
from pprint import pprint

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_data_info(url="https://index.minfin.com.ua/ua/markets/fuel/reg/volynskaya/"):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    items = soup.find("table")

    fuels = {}

    for row in items.find_all("tr")[1:]:
        cols = row.find_all("td")
        fuel_type = cols[0].text.strip()
        price = cols[1].text.strip()
        change = cols[2].text.strip()
        change_percent = cols[3].text.strip()
        
        fuels[fuel_type] = {
            "price": price,
            "change": change,
            "change_percent": change_percent
        }

    return fuels

if __name__ == "__main__":
    items = get_data_info()
    for fuel, info in items.items():
        print(f"{fuel:<25}: {info['price']:>7} грн, зміна: {info['change']:>6} ({info['change_percent']:>6})")