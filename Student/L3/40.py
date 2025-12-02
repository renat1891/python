import requests
from bs4 import BeautifulSoup
import time
import random

API = "BF0NoHRou+c6gR4NAbDT8g==L5W5JTQqii6A4oFT"


def get_joke():
    print("Fetching joke...")
    url = "https://api.api-ninjas.com/v1/jokes"
    headers = {"X-Api-Key": API}
    response = requests.get(url, headers=headers)
    joke = response.json()[0]["joke"]
    return joke

def get_fact():
    print("Fetching fact...")
    url = "https://api.api-ninjas.com/v1/facts"
    headers = {"X-Api-Key": API}
    response = requests.get(url, headers=headers)
    fact = response.json()[0]["fact"]
    return fact

while True:
    if random.randint(0,1)==0:
        choice = get_joke()
    else:
        choice = get_fact()        
    print(choice)
    time.sleep(10)