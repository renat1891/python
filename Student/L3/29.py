import requests
from bs4 import BeautifulSoup


link = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"



response = requests.get(link)
html = response.text
soup = BeautifulSoup(html, 'lxml')
cards = soup.find_all('div', class_='card')
for card in cards:
    title = card.find('a', class_='title').get_text().strip()
    price = card.find('h4', class_='price').get_text().strip()
    description = card.find('p', class_='description').get_text()
    link= card.find('a', class_='title')['href']
    print(f"Назва: {title}")
    print(f"Ціна: {price}")
    print(f"Опис: {description}")
    print(f"Посилання: https://webscraper.io{link}")
    print("-" * 40)



print(f"Знайдено товарів: {len(cards)}")