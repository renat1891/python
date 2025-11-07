# API

import requests
from tkinter import *


link = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"

response = requests.get(link)

print(response.status_code)

# data = response.text
data = response.json()
euro = float(data[0]["buy"])
usd = float(data[1]["buy"])

money = float(input("Enter amount in UAH: "))

print(f"You can buy {money / euro:.2f} EUR")
print(f"You can buy {money / usd:.2f} USD")