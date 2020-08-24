from tkinter import *
from tkinter import messagebox
from random import randint
from random import *
import time

globalspeedp = 0
globalspeedn = 0
norp = ''

class Ball():

    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False


    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        global count, pointcount
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.delete("all")
            canvas.create_text(250, 180, text = "You lost", width = 100, font = "Verdana 14")
            canvas.delete("all")
            tk.mainloop()

        if self.hit_paddle(pos) == True:
            if norp == 'n':
                self.y = globalspeedn
            else:
                self.y = globalspeedp * -1
            count += 1
            canvas.delete(pointcount)
            pointcount = canvas.create_text(480, 50, text=count)

        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)


    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0



    def turn_left(self, evt):
        global globalspeedn, norp
        notstarts = [-6, -5, -4, -3, -2]
        randnum = randint(0, 4)
        self.x = notstarts[randnum]
        globalspeedn = self.x
        norp = 'n'

    def turn_right(self, evt):
        global globalspeedp, norp
        notstarts = [6, 5, 4, 3, 2]
        randnum = randint(0, 4)
        self.x = notstarts[randnum]
        globalspeedp = self.x
        norp = 'p'


tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
count = 0
pointcount = canvas.create_text(480, 50, text = count)


tk.update()

def funccall(event):
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, paddle, 'red')

    while 1:
        ball.draw()
        paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

canvas.bind_all('<Button-1>', funccall)
tk.mainloop()
