import turtle
import random

t = turtle.Pen()

'''
t.goto(-200, -200)

while t.xcor() < 200:
    t.forward(10)
    t.up()
    t.forward(10)
    t.down()

t.up()
t.home()
t.forward(100)
t.down()

count = 0

while count < 4:
    t.forward(10)
    t.up()
    t.forward(10)
    t.down()
    t.forward(10)
    t.up()
    t.forward(10)
    t.down()
    t.left(90)
    count += 1
    
'''


'''
while t.xcor() < 200 or t.ycor() < 200:
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
'''


'''
n = int(input('How many fences do you want ? '))
count = 0

while count < n:
    t.left(90)
    t.forward(100)
    t.right(45)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(45)
    t.forward(100)
    t.left(90)
    count += 1
'''

'''
t.up()
t.left(90)
t.forward(250)
t.left(90)
t.forward(340)
t.down()
t.right(180)

n = int(input('Write a number'))

while n > 0:
    t.forward(n)
    t.right(90)
    n -= 10
'''
r = 100
count = 1
while count > 0:
    t.color((random.random(), random.random(), random.random()), (random.random(), random.random(), random.random()))
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    r -= 10
    count -= 1

t.reset()

r = 100
count = 5
while count > 0:
    t.color((random.random(), random.random(), random.random()), (random.random(), random.random(), random.random()))
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    r -= 10
    count -= 1
