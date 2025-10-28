from tkinter import * 
from tkinter import messagebox

def on_checkbutton_toggle():
    if var.get() == 1:
        messagebox.showinfo("Статус", "Включено")
    else:
        messagebox.showinfo("Статус", "Вимкнено")

root = Tk()
root.title("Checkbutton Demo")
root.geometry("300x200")

var = IntVar()

checkbutton = Checkbutton(
    root, 
    text="Включити", 
    variable=var,
    command=on_checkbutton_toggle
)
checkbutton.pack(pady=20)

root.mainloop()