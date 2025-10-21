from tkinter import *
from tkinter import messagebox

window = Tk()
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
    lb_result["text"] = f"{result:.2f} грн"
    messagebox.showinfo("Результат", f"{amount} {currency} = {result:.2f} грн")

Label(window, text="Виберіть валюту", font=("Arial", 12)).place(x=60, y=10)

var = IntVar()
var.set(1)
Radiobutton(window, text="долар", variable=var, value=1).place(x=40, y=40)
Radiobutton(window, text="євро", variable=var, value=2).place(x=120, y=40)

Label(window, text="Курс долара: 36.6").place(x=40, y=70)
Label(window, text="Курс євро: 40.5").place(x=40, y=90)

Label(window, text="Введіть суму у валюті:").place(x=40, y=120)
entry = Entry(window)
entry.place(x=60, y=140)

Button(window, text="Конвертувати", command=convert).place(x=70, y=170)

lb_result = Label(window, text="", font=("Arial", 14), fg="red")
lb_result.place(x=80, y=210)

mainloop()





























# from tkinter import *
# from tkinter import messagebox

# window = Tk()
# window.title("Вибір класу")
# window.geometry("300x250")

# selected_class = StringVar()
# selected_class.set("1")

# def show_choice():
#     choice = selected_class.get()
#     messagebox.showinfo("Ваш вибір", f"Ви обрали {choice} клас")

# for i in range(1, 11):
#     Radiobutton(window, text=f"{i} клас", variable=selected_class, value=str(i)).place(x=40, y=20 + i*20)

# Button(window, text="Підтвердити вибір", command=show_choice).place(x=80, y=220)

# window.mainloop()


































# from tkinter import *

# window = Tk()
# window.title("Зміна кольору фону")
# window.geometry("300x200")

# label = Label(window, text="Текст", font=("Arial", 16), bg="white", width=20, height=2)
# label.pack(pady=20)

# color_var = StringVar()
# color_var.set("white")  

# def change_color():
#     label.config(bg=color_var.get())

# colors = [
#     ("Синій", "blue"),
#     ("Жовтий", "yellow"),
#     ("Червоний", "red"),
#     ("Зелений", "green")
# ]

# for i, (color_name, color_value) in enumerate(colors):
#     Radiobutton(
#         window,
#         text=color_name,
#         variable=color_var,
#         value=color_value,
#         command=change_color
#     ).pack(anchor='w', padx=50)

# window.mainloop()










# from tkinter import *
# import random

# window = Tk()
# window.title("Вгадай число!")
# window.geometry("300x250")

# secret_number = random.randint(1, 100)
# attempts = 7


# Label(window, text="Вгадай число!", font=("Arial", 14, "bold")).pack(pady=10)
# Label(window, text="Я загадав число від 1 до 100").pack()

# Label(window, text=f"Залишилось спроб: {attempts}").pack()

# Label(window, text="Введи відповідь:").pack(pady=5)

# entry = Entry(window)
# entry.pack()

# result_label = Label(window, text="")
# result_label.pack(pady=10)

# def check_guess():
#     global attempts
    
#     try:
#         guess = int(entry.get())
#         attempts -= 1
        
#         if guess == secret_number:
#             result_label.config(text="Вітаю! Ви вгадали число!")
#         elif guess < secret_number:
#             result_label.config(text=f"Загадане число більше. Спроб: {attempts}")
#         else:
#             result_label.config(text=f"Загадане число менше. Спроб: {attempts}")
            
#         if attempts == 0 and guess != secret_number:
#             result_label.config(text=f"Гра закінчена! Число було: {secret_number}")
            
#     except:
#         result_label.config(text="Введіть число!")

# Button(window, text="Натисни", command=check_guess).pack(pady=5)

# window.mainloop()