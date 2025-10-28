import random
from tkinter import *


root = Tk()
root.title("tk")
root.geometry("400x200")

secret_number = random.randint(1, 50)
min_value = 1
max_value = 50

slider_value = IntVar()
slider_value.set(25)  


def check_guess():
    global min_value, max_value
    guess = slider_value.get()
    
    if guess == secret_number:
        result_label.config(text=f"Вітаю! Ви вгадали число {secret_number}!", fg="green")
        slider.config(state=DISABLED)
        check_button.config(state=DISABLED)
    elif guess < secret_number:
        min_value = guess + 1
        result_label.config(text=f"Загадане число БІЛЬШЕ ніж {guess}", fg="red")
        update_slider_range()
    else:
        max_value = guess - 1
        result_label.config(text=f"Загадане число МЕНШЕ ніж {guess}", fg="blue")
        update_slider_range()


def update_slider_range():
    slider.config(from_=min_value, to=max_value)
    new_value = (min_value + max_value) // 2
    slider_value.set(new_value)
    value_label.config(text=f"Обране число: {new_value}")
    
    if min_value == max_value:
        result_label.config(text=f"Залишилось тільки число {min_value}!", fg="orange")


def update_slider_value(value):
    value_label.config(text=f"Обране число: {int(float(value))}")

secret_label = Label(root, text="Загадане число: ?", font=("Arial", 10))
secret_label.grid(row=0, column=0, columnspan=2)

slider = Scale(root, from_=min_value, to=max_value, 
               orient=HORIZONTAL, length=300, variable=slider_value,
               command=update_slider_value, showvalue=0)
slider.grid(row=1, column=0, columnspan=2)

value_label = Label(root, text=f"Обране число: {slider_value.get()}", font=("Arial", 12))
value_label.grid(row=2, column=0, columnspan=2)

check_button = Button(root, text="Перевірити", command=check_guess, font=("Arial", 12))
check_button.grid(row=3, column=0, columnspan=2)

result_label = Label(root, text="", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2)

mainloop()