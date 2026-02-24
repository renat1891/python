import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.work.ua"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def parse_python_jobs(city="kyiv", limit=5):
    url = f"{BASE_URL}/jobs-{city}-python/"

    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "lxml")

        jobs = []
        cards = soup.select("div.card")

        for card in cards:
            title_tag = card.select_one("h2 a")
            if not title_tag:
                continue

            title = title_tag.text.strip()
            link = BASE_URL + title_tag["href"]

            company_tag = card.select_one("a.company")
            company = company_tag.text.strip() if company_tag else "—"

            salary_tag = card.select_one("span.salary")
            salary = salary_tag.text.strip() if salary_tag else "Не вказано"

            jobs.append({
                "title": title,
                "company": company,
                "salary": salary,
                "link": link
            })

            if len(jobs) >= limit:
                break

        return jobs

    except Exception as e:
        print("Помилка:", e)
        return []