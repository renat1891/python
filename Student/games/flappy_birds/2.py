from tkinter import *
from tkinter import messagebox

window = Tk()
window.title(" .....")
window.geometry("150x250")

def respawn():
    text = entry.get()
    lb2["text"] = "Вас звуть"+text
    messagebox.showinfo("Info", "Button Clicked!")
    messagebox.showwarning("Warning", "This is a warning message.")
    messagebox.showerror("Error", "This is an error message.")


btn = Button(window, text = "Згенерувати", command=respawn)
btn.place(x = 40, y = 120)

entry = Entry(window)
entry.place(x = 15, y = 80)

lb = Label(window, text="Введіть ім'я: ")
lb.place(x=40 , y=50)

lb2 = Label(window, text="-")
lb2.place(x=20 , y=160)
mainloop()