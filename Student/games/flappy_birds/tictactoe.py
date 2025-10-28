from tkinter import *
import random

class TicTacToe:
    def __init__(self, win):
        self.win = win
        win.title("Хрестики-нулики")
        self.player = random.choice(["X","O"])
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                b = Button(win,text="",font=("Arial",24),width=5,height=2)
                b.grid(row=i,column=j,padx=5,pady=5)
                row.append(b)
            self.buttons.append(row)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["command"] = self.make_click_handler(i,j)

        self.lbl = Label(win,text=self.get_turn_text(),font=("Arial",14))
        self.lbl.grid(row=3,column=0,columnspan=3)
        Button(win,text="Скинути",font=("Arial",12),command=self.reset).grid(row=4,column=0,columnspan=3)

        if self.player=="O":
            win.after(500,self.bot_move)

    def make_click_handler(self,i,j):
        def handler(): self.click(self.buttons[i][j])
        return handler

    def get_turn_text(self): return f"Хід: {'Ти' if self.player=='X' else 'Комп’ютер'}"

    def click(self,btn):
        if btn["text"]=="" and self.player=="X":
            btn["text"]="X"
            if self.check_win(): self.lbl.config(text="Ти переміг!"); self.disable_all()
            elif not any(b["text"]=="" for row in self.buttons for b in row): self.lbl.config(text="Нічия!")
            else: self.player="O"; self.lbl.config(text="Хід комп’ютера..."); self.win.after(500,self.bot_move)

    def bot_move(self):
        empty = [(i,j) for i in range(3) for j in range(3) if self.buttons[i][j]["text"]==""]
        if empty:
            i,j=random.choice(empty)
            self.buttons[i][j]["text"]="O"
            if self.check_win(): self.lbl.config(text="Комп’ютер переміг!"); self.disable_all()
            elif not any(b["text"]=="" for row in self.buttons for b in row): self.lbl.config(text="Нічия!")
            else: self.player="X"; self.lbl.config(text=self.get_turn_text())

    def check_win(self):
        for i in range(3):
            if self.buttons[i][0]["text"]==self.buttons[i][1]["text"]==self.buttons[i][2]["text"]!="": return True
            if self.buttons[0][i]["text"]==self.buttons[1][i]["text"]==self.buttons[2][i]["text"]!="": return True
        if self.buttons[0][0]["text"]==self.buttons[1][1]["text"]==self.buttons[2][2]["text"]!="": return True
        if self.buttons[0][2]["text"]==self.buttons[1][1]["text"]==self.buttons[2][0]["text"]!="": return True
        return False

    def disable_all(self):
        for row in self.buttons:
            for b in row: b.config(state=DISABLED)

    def reset(self):
        self.player=random.choice(["X","O"])
        self.lbl.config(text=self.get_turn_text())
        for row in self.buttons:
            for b in row: b.config(text="",state=NORMAL)
        if self.player=="O": self.win.after(500,self.bot_move)

win=Tk()
game=TicTacToe(win)
win.mainloop()
