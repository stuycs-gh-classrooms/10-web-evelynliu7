import turtle
import random
from random import randint

def draw_koch(t, depth, length):
    t.pd()
    if(depth==1):
        t.color(randint(200, 255),
                randint(100, 180),
                randint(100, 180))
        t.fd(length)
    else:
        draw_koch(t, depth-1, length)
        t.lt(30)
        draw_koch(t, depth-1, length)
        t.rt(150)
        draw_koch(t, depth-1, length)
        t.lt(30)
        draw_koch(t, depth-1, length)

def draw_sierpinski(t, depth, length):
    if (depth == 1):
        color = (randint(200, 255),
                 randint(100, 180),
                 randint(100, 180))
        t.fillcolor(color)
        t.pencolor(color)
        t.begin_fill()
        t.lt(60)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(180)
        t.end_fill()
    else:
        draw_sierpinski(t, depth-1, length/2)
        t.fd(length/2)
        draw_sierpinski(t, depth-1, length/2)
        t.bk(length/2)
        t.lt(60)
        t.fd(length/2)
        t.rt(60)
        draw_sierpinski(t, depth-1, length/2)
        t.fd(length/4)
        t.rt(180)
        draw_sierpinski(t, depth-1, length/4)
        t.fd(length/4)
        t.lt(60)
        t.fd(length/2)
        t.lt(120)

def tree(t, depth, length, angle, width):
    t.width(width)
    if(depth==1):
        t.color(randint(200, 255),
                randint(100, 180),
                randint(100, 180))
        t.fd(length)
        t.back(length)
        t.color(131, 67, 51)
    else:
        t.color(131, 67, 51)
        t.fd(length)
        t.lt(angle)
        tree(t, depth-1, length, angle, width-1)
        t.rt(2*angle)
        tree(t, depth-1, length, angle, width-1)
        t.lt(angle)
        t.bk(length)

spike=turtle.Turtle()
turtle.colormode(255)

spike.pu()
spike.goto(-300, 0)
spike.pd()
draw_sierpinski(spike, 4, 300)

# spike.width(3)
# spike.pu()
# spike.goto(-300, 300)
# spike.pd()
# spike.lt(45)
# draw_koch(spike, 4, 15)

# spike.color(131, 67, 51)
# tree(spike, 5, 50, 20, 8)

window = turtle.Screen()
window.exitonclick()