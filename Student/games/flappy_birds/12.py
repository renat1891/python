from customtkinter import *
from tkinter import messagebox


set_appearance_mode("dark")
set_default_color_theme("blue")

window = CTk()
window.title("Calculator")
window.geometry("400x500")

entry = CTkEntry(window, width=360, height=50, font=("Arial", 22), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

def add_to_entry(value):
    entry.insert("end", value)

def clear_entry():
    entry.delete(0, "end")

def calculate():
    try:
        expression = entry.get()
        if expression.strip() == "":
            messagebox.showinfo("Увага", "Введіть вираз для обчислення.")
            return
        result = eval(expression)
        entry.delete(0, "end")
        entry.insert(0, str(result))
    except Exception:
        messagebox.showerror("Помилка", "Некоректний вираз!")
        entry.delete(0, "end")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 0)
]

for (text, r, c) in buttons:
    CTkButton(window, text=text, width=80, height=60, font=("Arial", 20),
              command=lambda t=text: add_to_entry(t)).grid(row=r, column=c, padx=5, pady=5)

ops = [("+", 1), ("-", 2), ("/", 3), ("*", 4)]
for (op, r) in ops:
    CTkButton(window, text=op, width=80, height=60, font=("Arial", 20),
              fg_color="#ff4f81", hover_color="#ff6b9c",
              command=lambda o=op: add_to_entry(o)).grid(row=r, column=3, padx=5, pady=5)

CTkButton(window, text="=", width=80, height=60, font=("Arial", 20),
          fg_color="#1e88e5", hover_color="#42a5f5",
          command=calculate).grid(row=4, column=1, padx=5, pady=5)

CTkButton(window, text="clear", width=80, height=60, font=("Arial", 20),
          fg_color="#1e88e5", hover_color="#42a5f5",
          command=clear_entry).grid(row=4, column=2, padx=5, pady=5)

window.mainloop()
