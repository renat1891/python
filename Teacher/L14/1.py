from customtkinter import *

window = CTk()
window.title("Custom Tkinter")
window.geometry("400x300")


def button_event():
    print("button pressed")

button = CTkButton(window, text="CTkButton", command=button_event)
button.grid(row=0, column=0, padx=20, pady=20)


def switch_event():
   if(switch_var.get() == "on"):
       set_appearance_mode("light")
   else:
       set_appearance_mode("dark")

switch_var = StringVar(value="on")
switch = CTkSwitch(
    window, 
    text="CTkSwitch", 
    command=switch_event,
    variable=switch_var, 
    onvalue="on", 
    offvalue="off"
)
switch.grid(row=1, column=0, padx=20, pady=20)


window.mainloop()