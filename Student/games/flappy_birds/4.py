from tkinter import *


window = Tk()
window.title("Grid!")
window.geometry("300x250")

btn1 = Button(window, text = "1")
btn2 = Button(window, text = "2")
btn3 = Button(window, text = "3")
btn4 = Button(window, text = "4")
btn5 = Button(window, text = "5")
btn6 = Button(window, text = "6")
btn7 = Button(window, text = "7")
btn8 = Button(window, text = "8")
btn9 = Button(window, text = "9")

btn7.grid(row=0, column=0)
btn8.grid(row=0, column=1)
btn9.grid(row=0, column=2)
btn4.grid(row=1, column=0, rowspan=2, sticky= "ns", padx= 15, pady=15)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn2.grid(row=2, column=1, columnspan=2, sticky="ew")

mainloop()