import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.work.ua"

headers = {
    "User-Agent": "Mozilla/5.0"
}


def get_python_jobs(city="kyiv", limit=20):
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

            if "python" not in title.lower():
                continue

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

        if not jobs:
            raise ValueError("Вакансії не знайдені")

        return jobs

    except requests.exceptions.RequestException as e:
        print(f"HTTP помилка: {e}")
    except Exception as e:
        print(f"Помилка парсингу: {e}")

    return []


def get_latest_job(url):
    """
    Повертає одну (найпершу) вакансію
    """
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")

        card = soup.select_one("div.card")

        title_tag = card.select_one("h2 a")
        title = title_tag.text.strip()
        link = BASE_URL + title_tag["href"]

        company_tag = card.select_one("a.company")
        company = company_tag.text.strip() if company_tag else "—"

        salary_tag = card.select_one("span.salary")
        salary = salary_tag.text.strip() if salary_tag else "Не вказано"

        return title, company, salary, link

    except requests.exceptions.RequestException as e:
        print(f"HTTP помилка: {e}")
    except Exception as e:
        print(f"Помилка: {e}")

    return None