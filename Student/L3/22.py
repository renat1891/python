import customtkinter as ctk
import requests
from datetime import datetime
from tkinter import messagebox

API_KEY = "b40293aac1447231f0b72c74bbd827c6"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Weather App")
root.geometry("500x420")

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Помилка", "Введіть назву міста!")
        return
    
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "lang": "en"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Помилка", f"Місто не знайдено: {city}")
            return
        
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        visibility = round(data["visibility"] / 1000, 1)
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M %p")
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M %p")
        city_name = data["name"]
        country = data["sys"]["country"]
        now = datetime.now().strftime("%d/%m/%y   %I:%M %p")

        location_label.configure(text=f"{city_name}, {country}")
        datetime_label.configure(text=now)
        temp_label.configure(text=f"{int(temp)}°C")
        feels_label.configure(text=f"Feels like {int(feels_like)}° | {description}")
        humidity_label.configure(text=f"{humidity} %")
        pressure_label.configure(text=f"{pressure} mBar")
        desc_label.configure(text=description)
        visibility_label.configure(text=f"{visibility} km")
        sunrise_label.configure(text=sunrise)
        sunset_label.configure(text=sunset)

    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося отримати дані: {e}")

def reset_fields():
    city_entry.delete(0, ctk.END)
    for lbl in [location_label, datetime_label, temp_label, feels_label,
                humidity_label, pressure_label, desc_label, visibility_label,
                sunrise_label, sunset_label]:
        lbl.configure(text="")

frame_top = ctk.CTkFrame(root)
frame_top.pack(pady=10)

city_entry = ctk.CTkEntry(frame_top, width=250, placeholder_text="Введіть місто...")
city_entry.grid(row=0, column=0, padx=5)

search_btn = ctk.CTkButton(frame_top, text="", width=40, command=get_weather)
search_btn.grid(row=0, column=1, padx=5)

frame_info = ctk.CTkFrame(root, corner_radius=10)
frame_info.pack(pady=10, fill="x", padx=10)

location_label = ctk.CTkLabel(frame_info, text="", font=("Arial", 18, "bold"))
location_label.pack()

datetime_label = ctk.CTkLabel(frame_info, text="", font=("Arial", 14))
datetime_label.pack(pady=2)

temp_label = ctk.CTkLabel(frame_info, text="--°C", font=("Arial", 48, "bold"))
temp_label.pack(pady=5)

feels_label = ctk.CTkLabel(frame_info, text="", font=("Arial", 14))
feels_label.pack(pady=2)

frame_bottom = ctk.CTkFrame(root)
frame_bottom.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(frame_bottom, text="Humidity:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=5)
humidity_label = ctk.CTkLabel(frame_bottom, text="")
humidity_label.grid(row=0, column=1)

ctk.CTkLabel(frame_bottom, text="Pressure:", font=("Arial", 14)).grid(row=0, column=2, padx=10, pady=5)
pressure_label = ctk.CTkLabel(frame_bottom, text="")
pressure_label.grid(row=0, column=3)

ctk.CTkLabel(frame_bottom, text="Description:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=5)
desc_label = ctk.CTkLabel(frame_bottom, text="")
desc_label.grid(row=1, column=1)

ctk.CTkLabel(frame_bottom, text="Visibility:", font=("Arial", 14)).grid(row=1, column=2, padx=10, pady=5)
visibility_label = ctk.CTkLabel(frame_bottom, text="")
visibility_label.grid(row=1, column=3)

ctk.CTkLabel(frame_bottom, text="Sunrise:", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=5)
sunrise_label = ctk.CTkLabel(frame_bottom, text="")
sunrise_label.grid(row=2, column=1)

ctk.CTkLabel(frame_bottom, text="Sunset:", font=("Arial", 14)).grid(row=2, column=2, padx=10, pady=5)
sunset_label = ctk.CTkLabel(frame_bottom, text="")
sunset_label.grid(row=2, column=3)

btn_frame = ctk.CTkFrame(root)
btn_frame.pack(pady=15)

reset_btn = ctk.CTkButton(btn_frame, text="Reset", fg_color="#FFB000", hover_color="#FF9500", command=reset_fields)
reset_btn.grid(row=0, column=0, padx=10)

exit_btn = ctk.CTkButton(btn_frame, text="Exit", fg_color="#FF4C4C", hover_color="#E23C3C", command=root.destroy)
exit_btn.grid(row=0, column=1, padx=10)

root.mainloop()
