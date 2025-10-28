from customtkinter import *
import subprocess
import sys
import os

set_appearance_mode("dark")
set_default_color_theme("blue")

app = CTk()
app.title(" Game Menu")
app.geometry("500x500")

main_frame = CTkFrame(app)
main_frame.pack(fill="both", expand=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_flappy():
    subprocess.Popen([sys.executable, os.path.join(BASE_DIR, "flappy.py")])

def run_platformer():
    subprocess.Popen([sys.executable, os.path.join(BASE_DIR, "platformer.py")])

def run_tictactoe():
    subprocess.Popen([sys.executable, os.path.join(BASE_DIR, "tictactoe.py")])

CTkLabel(main_frame, text=" Вибери гру", font=("Arial", 30, "bold")).pack(pady=40)

CTkButton(main_frame, text=" Flappy Bird", command=run_flappy, width=200, height=50).pack(pady=10)
CTkButton(main_frame, text=" Платформер", command=run_platformer, width=200, height=50).pack(pady=10)
CTkButton(main_frame, text=" Хрестики-Нулики", command=run_tictactoe, width=200, height=50).pack(pady=10)

app.mainloop()

