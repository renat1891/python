import requests
from bs4 import BeautifulSoup
import json
import csv


link = "https://webscraper.io/test-sites/tables/tables-semantically-correct"

response = requests.get(link)
soup = BeautifulSoup(response.text, "lxml")

rows = soup.find_all("tr")[1:]  

users = []  

for row in rows:
    cols = row.find_all("td")
    if len(cols) >= 3:
        first_name = cols[0].get_text(strip=True)
        last_name = cols[1].get_text(strip=True)
        username = cols[2].get_text(strip=True)

        print(f"Ім'я: {first_name}")
        print(f"Прізвище: {last_name}")
        print(f"Нікнейм: {username}")
        print("-" * 40)

        users.append({
            "first_name": first_name,
            "last_name": last_name,
            "username": username
        })

print(f"Знайдено користувачів: {len(users)}")

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=4)

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["first_name", "last_name", "username"])
    writer.writeheader()
    writer.writerows(users)

print("Дані збережено у файли: users.json і users.csv")

