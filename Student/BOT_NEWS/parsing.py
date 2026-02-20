import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_data_info(url="https://www.pravda.com.ua/news/", category=""):
    r = requests.get(url+category, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    items = soup.select_one("div.article_news_list")
    time = items.select_one("div.article_time").text
    event = items.select_one("div.article_title").text.strip().split("\n")[-1].strip()
    link = items.select_one("a")["href"]

    return time, event, link

if __name__ == "__main__":
    time, event, link = get_data_info(category="mezha")
    print(f"Час: {time}\nПодія: {event}\nПосилання: {link}")