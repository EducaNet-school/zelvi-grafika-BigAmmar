import turtle

def op(a):
    turtle.forward(a)
    turtle.rt(90)
    turtle.forward(a)

a=5
while a != 125:
    op(a)
    a += 5
