import requests
from bs4 import BeautifulSoup




link = f"https://auto.ria.com/uk/search/?search_type=1&category=1&bodystyle[0]=5&price[0]=1&price[1]=9898&price[2]=9899&abroad=0&customs_cleared=1&page=0&limit=20"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(link, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

items = soup.find_all("a", class_="product-card")[0]

img = items.find("img").get("src")

print(img)

# title = items.find("div", class_="titleS").text
# print(title)

# print(items.text)



# BTC
