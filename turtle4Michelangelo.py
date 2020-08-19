import turtle
import random

a = turtle.Pen()
b = turtle.Pen()
c = turtle.Pen()

a.pencolor('blue')
b.pencolor('red')
c.pencolor('green')
a.width(5)
b.width(10)
c.width(15)
a.speed(1)
b.speed(1)
c.speed(1)

a.up()
a.goto(-300, 50)
a.down()

b.up()
b.goto(-300, 0)
b.down()


c.pencolor('black')
c.up()
c.goto(200,-100)
c.down()
c.goto(200,100)
c.up()
c.goto(-300, -50)
c.down()
c.pencolor('green')

step_a = 1
step_b = 1
step_c = 1

while a.xcor() < 200 and b.xcor() < 200 and c.xcor() < 200:
    if random.randint(0, 1) == 1 and step_a < 7:
        step_a += 1
    elif step_a > 1:
        step_a -= 1

    if random.randint(0, 1) == 1 and step_b < 7:
        step_b += 1
    elif step_b > 1:
        step_b -= 1

    if random.randint(0, 1) == 1 and step_c < 7:
        step_c += 1
    elif step_c > 1:
        step_c -= 1

    a.forward(step_a)
    b.forward(step_b)
    c.forward(step_c)

if a.xcor() > b.xcor() and a.xcor() > c.xcor():
    b.hideturtle()
    c.hideturtle()
elif b.xcor() > a.xcor() and b.xcor() > c.xcor():
    a.hideturtle()
    c.hideturtle()
elif c.xcor() > a.xcor() and c.xcor() > b.xcor():
    a.hideturtle()
    b.hideturtle()
elif a.xcor() == b.xcor() and a.xcor() > c.xcor():
    c.hideturtle()
elif a.xcor() == c.xcor() and a.xcor() > b.xcor():
    b.hideturtle()
elif b.xcor() == c.xcor() and b.xcor() > a.xcor():
    a.hideturtle()
else:
    a.hideturtle()
    b.hideturtle()
    c.hideturtle()

inp = input()