from customtkinter import *
import subprocess
import sys
import os

class GameMenuApp:
    def __init__(self):
        set_appearance_mode("dark")
        set_default_color_theme("blue")

        self.app = CTk()
        self.app.title(" Game Menu")
        self.app.geometry("500x500")

        self.main_frame = CTkFrame(self.app)
        self.main_frame.pack(fill="both", expand=True)

        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        self.setup_ui()

    def setup_ui(self):
        CTkLabel(self.main_frame, text=" Вибери гру", font=("Arial", 30, "bold")).pack(pady=40)

        CTkButton(self.main_frame, text=" Flappy Bird", command=self.run_flappy, width=200, height=50).pack(pady=10)
        CTkButton(self.main_frame, text=" Платформер", command=self.run_platformer, width=200, height=50).pack(pady=10)
        CTkButton(self.main_frame, text=" Хрестики-Нулики", command=self.run_tictactoe, width=200, height=50).pack(pady=10)

    def run_flappy(self):
        subprocess.Popen([sys.executable, os.path.join(self.BASE_DIR, "flappy.py")])

    def run_platformer(self):
        subprocess.Popen([sys.executable, os.path.join(self.BASE_DIR, "platformer.py")])

    def run_tictactoe(self):
        subprocess.Popen([sys.executable, os.path.join(self.BASE_DIR, "tictactoe.py")])

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    game_menu = GameMenuApp()
    game_menu.run()

