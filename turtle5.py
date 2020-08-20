import turtle

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
