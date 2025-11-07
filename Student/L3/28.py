import requests
import deepl
import customtkinter as ctk

def translate_text():
    user_text = input_field.get("1.0", "end").strip()
    target_lang = lang_var.get()

    if not user_text:
        result_label.configure(text="Введіть текст для перекладу.")
        return

    try:
        auth_key = "41c4cbe6-2089-413d-8c8f-0d16d52ce24e:fx"
        deepl_client = deepl.DeepLClient(auth_key)
        result = deepl_client.translate_text(user_text, target_lang=target_lang.upper())
        result_label.configure(text=f"Переклад ({target_lang}): {result.text}")
    except Exception as e:
        result_label.configure(text=f"Помилка перекладу: {e}")

app = ctk.CTk()
app.title("Перекладач")
app.geometry("400x300")

input_label = ctk.CTkLabel(app, text="Введіть текст:")
input_label.pack(pady=5)
input_field = ctk.CTkTextbox(app, height=100)
input_field.pack(pady=5)

lang_var = ctk.StringVar(value="en")
lang_label = ctk.CTkLabel(app, text="Оберіть мову перекладу:")
lang_label.pack(pady=5)
lang_menu = ctk.CTkOptionMenu(app, variable=lang_var, values=["EN-GB", "DE"],
                              dynamic_resizing=False)
lang_menu.pack(pady=5)

translate_button = ctk.CTkButton(app, text="Перекласти", command=translate_text)
translate_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)

app.mainloop()