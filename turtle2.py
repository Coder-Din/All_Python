import turtle
import math

t = turtle.Pen()
area = int(input('Type down the area of our square: '))


t.forward(math.sqrt(area))
t.right(90)
t.forward(math.sqrt(area))
t.right(90)
t.forward(math.sqrt(area))
t.right(90)
t.forward(math.sqrt(area))
t.right(90)

'''
length = int(input('How long should our square be ?'))

t = turtle.Pen()

t.forward(length)
t.right(90)
t.forward(length)
t.right(90)
t.forward(length)
t.right(90)
t.forward(length)
t.right(90)
'''

'''
t.color('green', 'green')

t.begin_fill()
t.circle(20)
t.left(90)
t.forward(40)
t.right(90)
t.end_fill()

t.color('yellow', 'yellow')

t.begin_fill()
t.circle(20)
t.left(90)
t.forward(40)
t.right(90)
t.end_fill()

t.color('red', 'red')

t.begin_fill()
t.circle(20)
t.left(90)
t.forward(40)
t.right(90)
t.end_fill()

t.left(90)

t.up()
t.forward(5)
t.right(90)
t.down()

t.forward(25)
t.right(90)
t.forward(130)
t.right(90)
t.forward(50)
t.right(90)
t.forward(130)
t.right(90)
t.forward(50)
'''