import customtkinter as ctk
import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime
from PIL import Image, ImageTk
import webbrowser

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
images_folder = os.path.join(desktop, "images")
os.makedirs(images_folder, exist_ok=True)


def get_olx_data(text):
    link = f"https://www.olx.ua/uk/list/q-{text}/?search%5Border%5D=created_at:desc"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "lxml")

    container = soup.find("div", class_="css-1sw7q4x") 
    if not container:
        return None

    items = soup.find_all("div", class_="css-1sw7q4x")
    for item in items:
        if "топ" in item.get_text(strip=True).lower():
            continue

        title_tag = item.find("h6") or item.find("h3") or item.find("h4")
        price_tag = item.find("p", class_="css-ol6ynp") or item.find("p", class_="css-blr5zl")
        time_tag = item.find("div", class_="css-1e28vjt")
        link_tag = item.find("a")
        image_tag = item.find("img")

        if not (title_tag and price_tag and link_tag and image_tag):
            continue

        return {
            "title": title_tag.get_text(strip=True),
            "price": price_tag.get_text(strip=True),
            "time": time_tag.get_text(strip=True) if time_tag else "не вказано",
            "link": "https://www.olx.ua" + link_tag["href"],
            "image": image_tag.get("src") or image_tag.get("data-src")
        }
    return None


def search():
    query = input_field.get()
    if not query:
        return

    data = get_olx_data(query)
    if not data:
        title_label.configure(text="Оголошень не знайдено")
        price_label.configure(text="")
        time_label.configure(text="")
        photo_label.configure(image="", text="немає фото")
        link_button.configure(command=lambda: None)
        return

    title_label.configure(text=data["title"])
    price_label.configure(text=data["price"])
    time_label.configure(text=data["time"])
    link_button.configure(command=lambda: open_link(data["link"]))

    try:
        img_bytes = requests.get(data["image"]).content
        ext = ".png" if ".png" in data["image"] else ".jpg"
        filename = f"img_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
        filepath = os.path.join(images_folder, filename)

        with open(filepath, "wb") as f:
            f.write(img_bytes)

        img_pil = Image.open(filepath)
        img_pil = img_pil.resize((220, 220))  
        img = ImageTk.PhotoImage(img_pil)

        photo_label.configure(image=img, text="")
        photo_label.image = img

    except Exception as e:
        photo_label.configure(text=f"Помилка фото:\n{e}")


def open_link(url):
    webbrowser.open(url)

ctk.set_appearance_mode("dark")
window = ctk.CTk()
window.title("OLX Scanner")
window.geometry("900x550")

input_field = ctk.CTkEntry(window, width=400, height=40, placeholder_text="Введіть пошук...")
input_field.pack(pady=20)

search_button = ctk.CTkButton(window, text="Пошук", width=200, height=40, command=search)
search_button.pack()

frame = ctk.CTkFrame(window, width=800, height=350)
frame.pack(pady=20)

photo_label = ctk.CTkLabel(frame, text="фото", width=220, height=220)
photo_label.place(x=20, y=40)

title_label = ctk.CTkLabel(frame, text="заголовок", width=500, height=40, anchor="w")
title_label.place(x=260, y=40)

price_label = ctk.CTkLabel(frame, text="ціна", width=150, height=40)
price_label.place(x=260, y=100)

time_label = ctk.CTkLabel(frame, text="час", width=150, height=40)
time_label.place(x=260, y=160)

link_button = ctk.CTkButton(frame, text="посилання на оголошення", width=500, height=40)
link_button.place(x=150, y=260)

window.mainloop()
