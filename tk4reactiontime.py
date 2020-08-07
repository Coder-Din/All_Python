from tkinter import *
from random import *
from time import *

root = Tk()
canvas = Canvas(root, width = 500, height = 500)
canvas.pack()
falls = 0
y = 20
listt = []
def main():
    global ball
    ball = canvas.create_oval(225, 225, 275, 275, fill="black")
    root.after(randint(3000, 10000), set_time)

def set_time():
    global start_time
    canvas.itemconfig(ball, fill="red")
    start_time = time()
    canvas.bind_all('<Button-1>', timer)



def timer(event):
    global falls, y, listt
    print('hello')
    sec = round(time() - start_time, 3)
    listt.append(sec)
    av = round(float(sum(listt)) / len(listt), 3)
    if sec < 1:
        canvas.create_text(40, y, font="Arial 14", text=sec)
        y += 20
        canvas.create_text(100, y, font="Arial 14", text='Average num: ' + str(av))
        y += 20
    else:
        canvas.create_text(40, y, font="Arial 14", text=1)
        y += 20
        canvas.create_text(100, y, font="Arial 14", text='Average num:' + str(av))
        y += 20
        falls += 1
        print(falls)
        if falls > 5:
            falls = 1
            main()
    canvas.delete(ball)
    root.after(500, main)




main()
root.mainloop()