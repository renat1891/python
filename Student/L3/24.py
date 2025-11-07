import customtkinter as ctk
import requests

API_KEY = "BF0NoHRou+c6gR4NAbDT8g==L5W5JTQqii6A4oFT"

def get_fact():
    url = "https://api.api-ninjas.com/v1/facts"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    fact = response.json()[0]["fact"]
    label_result.configure(text=fact)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Випадковий факт")
app.geometry("500x300")

label_title = ctk.CTkLabel(app, text="Натисни кнопку, щоб отримати факт:", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

btn_get = ctk.CTkButton(app, text="Отримати факт", command=get_fact)
btn_get.pack(pady=10)

label_result = ctk.CTkLabel(app, text="", wraplength=450, justify="center")
label_result.pack(pady=20)

app.mainloop()


