import requests
from bs4 import BeautifulSoup

link = "https://webscraper.io/test-sites/e-commerce/static/computers/tablets"

# *.json або *.csv
response = requests.get(link)
html = response.text

soup = BeautifulSoup(html, "lxml")
count_page = int(soup.find("ul", class_="pagination").find_all("li")[-2].text.strip())

for page in range(1, count_page + 1):
    link = f"https://webscraper.io/test-sites/e-commerce/static/computers/tablets?page={page}"
    print(f"Сторінка {page}")
    
    response = requests.get(link)
    html = response.text

    soup = BeautifulSoup(html, "lxml")
    cards = soup.find_all("div", class_="card")

    for card in cards:
        price = card.find("h4", class_="price").text.strip()
        title = card.find("a").text.strip()
        print(title, price)
    print("-" * 40)

