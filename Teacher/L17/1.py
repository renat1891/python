import requests
from bs4 import BeautifulSoup

link = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

response = requests.get(link)
html = response.text
# print(response.status_code)

soup = BeautifulSoup(html, "lxml")

container = soup.find("div", class_="container test-site")
cards = container.find_all("div", class_="row")[1]

for card in cards.find_all("div", class_="card"):
    price = card.find("h4", class_="price").text.strip()
    title = card.find("a").text.strip()
    print(title, price)

# print(len(cards.find_all("div", class_="card")))