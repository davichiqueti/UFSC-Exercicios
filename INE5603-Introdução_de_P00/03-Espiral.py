import turtle


constructor = turtle.Turtle()
constructor.speed(100)
constructor.pensize(2)
x = 40

for i in range(160):

    constructor.forward(x)
    constructor.right(93)
    x += 2

turtle.done()