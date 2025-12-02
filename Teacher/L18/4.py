import requests
from bs4 import BeautifulSoup
import time
import random

API = "BF0NoHRou+c6gR4NAbDT8g==L5W5JTQqii6A4oFT"


def get_joke():
    print("Отримуємо жарт")
    url = "https://api.api-ninjas.com/v1/jokes"
    headers = {"X-Api-Key": API}
    response = requests.get(url, headers=headers)
    joke = response.json()[0]["joke"]
    return joke

def get_fact():
    print("Отримуємо факт")
    url = "https://api.api-ninjas.com/v1/facts"
    headers = {"X-Api-Key": API}
    response = requests.get(url, headers=headers)
    fact = response.json()[0]["fact"]
    return fact

while True:
    joke = get_joke()
    fact = get_fact()
    random_choice = random.choice([joke, fact])
    print(random_choice)
    time.sleep(10)
