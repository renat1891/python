from customtkinter import *

set_appearance_mode("dark")       
set_default_color_theme("blue")   


app = CTk()
app.title("my app.")
app.geometry("420x250")


main_frame = CTkFrame(app)
main_frame.grid(row=0, column=0, padx=20, pady=20)


values_frame = CTkFrame(main_frame)
values_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

label_values = CTkLabel(values_frame, text="Values")
label_values.grid(row=0, column=0, pady=(10, 5))

check1 = CTkCheckBox(values_frame, text="value 1")
check1.grid(row=1, column=0, sticky="w", padx=10, pady=5)

check2 = CTkCheckBox(values_frame, text="value 2")
check2.grid(row=2, column=0, sticky="w", padx=10, pady=5)

check3 = CTkCheckBox(values_frame, text="value 3")
check3.grid(row=3, column=0, sticky="w", padx=10, pady=5)

options_frame = CTkFrame(main_frame)
options_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ns")

label_options = CTkLabel(options_frame, text="Options")
label_options.grid(row=0, column=0, pady=(10, 5))

radio_var = StringVar(value="option 1")

radio1 = CTkRadioButton(options_frame, text="option 1", variable=radio_var, value="option 1")
radio1.grid(row=1, column=0, sticky="w", padx=10)

radio2 = CTkRadioButton(options_frame, text="option 2", variable=radio_var, value="option 2")
radio2.grid(row=2, column=0, sticky="w", padx=10)


button = CTkButton(app, text="my button")
button.grid(row=1, column=0, padx=20, pady=(0, 20))

app.mainloop()