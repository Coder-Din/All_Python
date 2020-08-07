from datetime import *
from time import *
from random import *
from tkinter import *

root = Tk()
messages = [
    "Out of all the trees, we bumped only into 1",
    "If you will not try to save him, he won't be tried to save",
    "I am a magician, not a circus monkey",
    "Dreams are our visions of perfect world",
    "Nightmares are our visions of awful world",
    "One action values more than a hundred words"
]

def main():
    label1 = Label(text = "Checking your speed of typing. Type down the following phrase. I will start the timer...")
    label1.pack()
    root.after(2000, func2)

def func2():
    label2 = Label(text = "Ready...")
    label2.pack()
    root.after(1, func3)

def func3():
    global messages, message, entry, start_time
    label3 = Label(text = "Start:")
    label3.pack()
    message = messages[randint(0, 5)]
    label4 = Label(text = message)
    label4.pack()
    start_time = datetime.now()
    entry = Entry(width = 60)
    entry.pack()
    root.bind('<Return>', entryfunc)

def entryfunc(event):
    answer = entry.get()
    end_time = datetime.now()
    delta = end_time - start_time
    seconds = delta.seconds + delta.microseconds / 1000000
    speed = round(len(answer) / seconds, 2)
    label5 = Label(text = 'You typed ' + str(len(answer)) + ' symbols in ' + str(round(seconds, 1)) + ' seconds')
    label5.pack()
    label6 = Label(text = str(speed) + ' symbols per second')
    label6.pack()
    if message == answer:
        label = Label(text = 'And you had no errors!')
        label.pack()
    else:
        label = Label(text = 'But you had at least one error')
        label.pack()


main()
root.mainloop()