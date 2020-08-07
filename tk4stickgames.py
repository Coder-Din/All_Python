from tkinter import *
from random import *
root = Tk()
root.title('Stick game')
root.geometry('300x200')
root.configure(bg = 'green')

num = 20

def comp_turn():
    global num
    randnum = randint(1,3)
    num -= randnum
    if (num == 1):
        label1.config(text = 'You lost')
        label2.config(text = 'You lost')
        label3.config(text = 'You lost')
    else:
        label1.config(text = 'Write a number 1-3')
        label2.config(text = num * '|')
        label3.config(text = str(num))

def user():
    global num
    totake = int(entry.get())
    if (totake < 4):
        num -= totake
        label2.config(text = num * '|')
        label3.config(text = str(num))
        if (num == 1):
            label1.config(text = 'You won')
            label2.config(text = 'You won')
            label3.config(text = 'You won')
        else:
            label1.config(text = 'Computer turn')
            root.after(2000, lambda: comp_turn())
    else:
        label1.config(text = 'ERROR')
        label2.config(text = 'ERROR')
        label3.config(text = 'ERROR')

label1 = Label(text = 'Write a number 1-3')
label2 = Label(root, text = num * '|')
label3 = Label(text = num)
entry = Entry(width = 10)
button = Button(text = 'Take the sticks', command = user)


label1.pack()
entry.pack()
label2.pack()
label3.pack()
button.pack()

root.mainloop()