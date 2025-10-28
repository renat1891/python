from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("My First GUI Program")
window.geometry("400x300")

def respawn():
    text = entry.get()
    lb["text"] = text
    messagebox.showinfo("Info", "Button Clicked!")
    messagebox.showwarning("Warning", "This is a warning message.")
    messagebox.showerror("Error", "This is an error message.")

btn = Button(window, text="Click Me", command=respawn)
btn.place(x=150, y=130)

entry = Entry(window)
entry.place(x=150, y=100)

lb = Label(window, text="Hello, Tkinter!", fg="blue", bg="green")
lb.place(x=170, y=70)


mainloop()

# place x y
# pack 
# grid 