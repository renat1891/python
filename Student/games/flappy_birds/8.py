from tkinter import *
import random

root = Tk()
root.title("Камінь, ножиці, папір")
root.geometry("300x300")

wins = 0
losses = 0
ties = 0

def determine_winner(player, computer):
    if player == computer:
        return "нічия"
    
    winning_combinations = {
        "камінь": "ножиці",
        "ножиці": "папір", 
        "папір": "камінь"
    }
    
    if winning_combinations[player] == computer:
        return "перемога"
    else:
        return "поразка"

def play_rock():
    play_game("камінь")

def play_scissors():
    play_game("ножиці")

def play_paper():
    play_game("папір")

def play_game(player_choice):
    global wins, losses, ties
    
    choices = ["камінь", "ножиці", "папір"]
    computer_choice = random.choice(choices)
    
    result = determine_winner(player_choice, computer_choice)
    
    if result == "перемога":
        wins += 1
    elif result == "поразка":
        losses += 1
    else:
        ties += 1
    
    wins_label.config(text=f"Перемог: {wins}")
    losses_label.config(text=f"Поразок: {losses}")
    ties_label.config(text=f"Нічиїх: {ties}")
    
    status_text = {
        "перемога": "Ви перемогли!",
        "поразка": "Ви програли!", 
        "нічия": "Нічия!"
    }
    status_label.config(text=status_text[result])


title_label = Label(root, text="Камінь, ножиці, папір", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3)

wins_label = Label(root, text=f"Перемог: {wins}", font=("Arial", 12))
wins_label.grid(row=1, column=0)

losses_label = Label(root, text=f"Поразок: {losses}", font=("Arial", 12))
losses_label.grid(row=1, column=1)

ties_label = Label(root, text=f"Нічиїх: {ties}", font=("Arial", 12))
ties_label.grid(row=1, column=2)

status_label = Label(root, text="Початок гри!", font=("Arial", 14, "bold"))
status_label.grid(row=2, column=0, columnspan=3)

rock_btn = Button(root, text="Камінь", font=("Arial", 12), command=play_rock)
rock_btn.grid(row=3, column=0)

scissors_btn = Button(root, text="Ножиці", font=("Arial", 12), command=play_scissors)
scissors_btn.grid(row=3, column=1)

paper_btn = Button(root, text="Папір", font=("Arial", 12), command=play_paper)
paper_btn.grid(row=3, column=2)


mainloop()