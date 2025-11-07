from customtkinter import *
from tkinter import messagebox
import requests

window = CTk()

def get_weather():
    city_name = ent.get()
    API_key = "1954bdc71a2b87b31d8815f9073ae54c"


    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang=ua"

    response = requests.get(url)
    data = response.json()


    weather=data["weather"][0]['description']
    temp=data["main"]['temp']
    lb.configure(text=f"temp{temp}, weather{weather}")



CTkButton(window, text="Визначити", width=80, height=60, font=("Arial", 20), command=get_weather).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
lb=CTkLabel(window,text='натисніть на кнопку')
lb.grid(row=1, column=1)
ent=CTkEntry(window)
ent.grid(row=3, column=2)


window.mainloop()