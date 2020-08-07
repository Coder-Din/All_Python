from tkinter import *
from tkinter import messagebox
import random
import threading
import time
root = Tk()

score = 3

def restart(score):
    global wins, buttons
    numbers = [i for i in range(1, score**2+1)]
    wins = [i for i in range(1, score**2+1)]
    random.shuffle(numbers)
    buttons = []
    x = 0
    y = 0
    for id, item in enumerate(numbers):
        btn = Button(root, text=item, height=3, width=6, command=lambda idx=id, num=item: binding(idx, num))
        btn.grid(row=y*50, column=x*50)
        buttons.append(btn)
        x += 1
        if x == score:
            x = 0
            y += 1


def binding(idx, num):
    global wins, buttons, score
    if wins[0] == num:
        buttons[idx].config(bg = '#ffffff')
        del wins[0]
    else:
        messagebox.showerror('Упс', "Ты не правильно ввел\nпридется начать сначала")

        restart(score)
    if len(wins) == 0:
        score += 1
        restart(score)
        messagebox.showinfo('Nice', 'You won!')





restart(score)
root.mainloop()