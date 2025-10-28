from tkinter import *

window = Tk()
window.title("Grid!")
window.geometry("300x250")

btn1 = Button(window, text="Button 1")
btn3 = Button(window, text="Button 3", width=20)
btn4 = Button(window, text="Button 4")

btn1.grid(row=0, column=0, columnspan=2, sticky="we", pady=15, padx=15)
btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)

mainloop()