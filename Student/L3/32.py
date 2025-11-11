from bs4 import BeautifulSoup
import requests

def get_olx_data(text):
    link = f"https://www.olx.ua/uk/list/q-{text}/?search%5Border%5D=created_at:desc"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    item_container = soup.find('div', class_='css-j0t2x2')
    items = item_container.find_all('div', class_='css-1sw7q4x')

    first_ad = {}
    for item in items:
        title_tag = item.find('h4', class_='css-hzlye5')
        price_tag = item.find('p', class_='css-blr5zl')
        time_tag = item.find('div', class_='css-acsxuw')
        link_tag = item.find('a', class_='css-1tqlkj0')['href']
        img_tag = item.find('img', class_='css-8wsg1m')['src']
        istop = item.find('div', class_='css-1ut25fa')

        title = title_tag.get_text(strip=True) if title_tag else "Немає назви"
        price = price_tag.get_text(strip=True) if price_tag else "Немає ціни"
        link_full = "https://www.olx.ua" + link_tag if link_tag else "Немає посилання"
        img_url = img_tag if img_tag else "Немає зображення"
        time = time_tag.get_text(strip=True) if time_tag else "Немає часу"

        first_ad = {
            "title": title,
            "price": price,
            "link": link_full,
            "image": img_url,
            "time": time
        }
        if "топ" not in istop.get_text(strip=True).lower():
            break

    return first_ad

if __name__ == "__main__": 
    search_text = input("Введіть пошуковий запит: ")
    data = get_olx_data(search_text)
    print(f"Назва: {data['title']}")
    print(f"Ціна: {data['price']}")
    print(f"Посилання: {data['link']}")
    print(f"Зображення: {data['image']}")
    print(f"Час: {data['time']}")
    
    
