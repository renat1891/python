import customtkinter as ctk
import requests
import deepl

API_KEY = "BF0NoHRou+c6gR4NAbDT8g==L5W5JTQqii6A4oFT"

def get_fact():
    url = "https://api.api-ninjas.com/v1/facts"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    print("Get Fact Response Status Code:", response.status_code)
    fact = response.json()[0]["fact"]
    label_title1.configure(text=fact)
    fact_uk = translate_fact(fact, target_lang='uk')
    label_title2.configure(text=fact_uk)
    fact_pl = translate_fact(fact, target_lang='pl')
    label_title3.configure(text=fact_pl)
    



def translate_fact(fact, target_lang):
    auth_key = "41c4cbe6-2089-413d-8c8f-0d16d52ce24e:fx"
    deepl_client = deepl.DeepLClient(auth_key)

    result = deepl_client.translate_text(fact, target_lang=target_lang)
    return result.text

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Випадковий факт")
app.geometry("500x300")

label_title1 = ctk.CTkLabel(app, text="Натисни кнопку, щоб отримати факт:", font=("Arial", 16, "bold"))
label_title1.pack(pady=10)

label_title2 = ctk.CTkLabel(app, text="Натисни кнопку, щоб отримати факт:", font=("Arial", 16, "bold"))
label_title2.pack(pady=20)

label_title3 = ctk.CTkLabel(app, text="Натисни кнопку, щоб отримати факт:", font=("Arial", 16, "bold"))
label_title3.pack(pady=25)

btn_get = ctk.CTkButton(app, text="Отримати факт", command=get_fact)
btn_get.pack(pady=10)

label_result = ctk.CTkLabel(app, text="", wraplength=450, justify="center")
label_result.pack(pady=20)

app.mainloop()
