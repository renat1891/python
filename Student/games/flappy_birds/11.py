# from customtkinter import * 

# app = CTk()
# app.geometry("600x500")
# app.title("CTk example")

# def slider_event(value):
#     ties_label.configure(text=value)

# slider = CTkSlider(app, from_=0, to=100, command=slider_event)

# slider.grid(row=3, column=2)
# ties_label = CTkLabel(app, text="")
# ties_label.grid(row = 4, column=3)


# app.mainloop()

from customtkinter import * 
from tkinter import messagebox

window = CTk()
window.title("Конвертер валют")
window.geometry("250x250")

USD = 36.6
EUR = 40.5

def convert():
    text = entry.get()
    if text == "":
        messagebox.showinfo("Увага", "Введіть суму для конвертації.")
        return
    
    amount = float(text)
    if var.get() == 1:
        rate = USD
        currency = "долар"
    else:
        rate = EUR
        currency = "євро"

    result = amount * rate
    lb_result.configure(text=  f"{result:.2f} грн")
    messagebox.showinfo("Результат", f"{amount} {currency} = {result:.2f} грн")

CTkLabel(window, text="Виберіть валюту", font=("Arial", 12)).place(x=60, y=10)

var = IntVar()
var.set(1)
CTkRadioButton(window, text="долар", variable=var, value=1).place(x=40, y=40)
CTkRadioButton(window, text="євро", variable=var, value=2).place(x=120, y=40)

CTkLabel(window, text="Курс долара: 36.6").place(x=40, y=70)
CTkLabel(window, text="Курс євро: 40.5").place(x=40, y=90)


CTkLabel(window, text="Введіть суму у валюті:").place(x=40, y=120)
entry = CTkEntry(window)
entry.place(x=60, y=140)

CTkButton(window, text="Конвертувати", command=convert).place(x=70, y=170)

lb_result = CTkLabel(window, text="", font=("Arial", 14), fg_color="red")
lb_result.place(x=80, y=210)

window.mainloop()

