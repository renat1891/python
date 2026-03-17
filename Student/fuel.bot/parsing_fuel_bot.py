import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_data_info(url="https://index.minfin.com.ua/ua/markets/fuel/reg/", category=""):
    r = requests.get(url+category, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    items = soup.select_one("table")
    rows = items.find_all("tr")[1:]
    fuels = {}
    for row in rows:
        cols = row.find_all("td")
        fuel_type = cols[0].text.strip()
        price = cols[1].text.strip()
        change = cols[2].text.strip()
        change_precent = cols[3].text.strip()
        fuels[fuel_type] = {"price": price, "change": change, "change_percent": change_precent}
    return fuels





if __name__ == "__main__":
    fuels = get_data_info()
    for fuel_type, data in fuels.items():
        print(f"{fuel_type:_<10}: {data['price']}, {data['change']}, {data['change_percent']}")

    