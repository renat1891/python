from tkinter import * 
root = Tk()
root.geometry("300x300")

mainmenu = Menu(root)

root.config(menu = mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Новий")
filemenu.add_separator()
filemenu.add_command(label="Новий")
filemenu.add_command(label="Довідка")


mainmenu.add_cascade(label="Файл", menu=filemenu)

mainloop()