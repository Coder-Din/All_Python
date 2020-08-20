import turtle
import random

'''

c = int(input('How many figures do you want: '))
n = int(input('How many sides will our figure have: '))

t = turtle.Pen()
t.speed(1)

for i in range(c):
    for i in range(n):
        t.forward(10)
        t.left(360/n)
    t.up()
    t.forward(100)
    t.down()

a = input()

'''

t = turtle.Pen()
n = int(input('How many figures will we have: '))

for i in range(n):
    t.color((random.random(), random.random(), random.random()), (random.random(), random.random(), random.random()))
    t.begin_fill()
    for i in range(11):
        t.fd(30)
        t.rt(32.727)
    t.end_fill()
    t.rt(360/n)
