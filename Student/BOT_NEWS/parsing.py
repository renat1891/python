import requests
from bs4 import BeautifulSoup



headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_data_info(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    items = soup.select_one("div.article_news_list")
    time = items.select_one("div.article_time").text
    event = items.select_one("div.article_title").text.strip().split("\n")[-1].strip()
    link = items.select_one("a")["href"]

    return time, event, link

def fetch_multiple_articles(url):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")

        articles = []
        items = soup.select("div.article_news_list")
        for item in items:
            time = item.select_one("div.article_time")
            event = item.select_one("div.article_title")
            link = item.select_one("a")

            if time and event and link:
                articles.append((
                    time.text,
                    event.text.strip().split("\n")[-1].strip(),
                    link["href"]
                ))

        if not articles:
            raise ValueError("Немає оголошень")

        return articles

    except requests.exceptions.RequestException as e:
        print(f"HTTP Запит відхилиний: {e}")
    except Exception as e:
        print(f"Виникла помилка: {e}")

    return []

def fetch_latest_news(url, headers):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")

        articles = []
        items = soup.select("div.article_news_list")
        for item in items:
            time = item.select_one("div.article_time")
            event = item.select_one("div.article_title")
            link = item.select_one("a")

            if time and event and link:
                articles.append((
                    time.text,
                    event.text.strip().split("\n")[-1].strip(),
                    link["href"]
                ))

        return articles

    except requests.exceptions.RequestException as e:
        print(f"HTTP Запит відхилиний: {e}")
    except Exception as e:
        print(f"Виникла помилка: {e}")

    return []