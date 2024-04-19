import turtle
import random
from random import randint

def original_draw_koch(t, depth, length):
    t.pd()
    if(depth==1):
        t.fd(length)
    else:
        original_draw_koch(t, depth-1, length)
        t.lt(60)
        original_draw_koch(t, depth-1, length)
        t.rt(120)
        original_draw_koch(t, depth-1, length)
        t.lt(60)
        original_draw_koch(t, depth-1, length)

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

def original_draw_sierpinski(t, depth, length):
    if (depth == 1):
        t.lt(60)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(180)
    else:
        original_draw_sierpinski(t, depth-1, length/2)
        t.fd(length/2)
        original_draw_sierpinski(t, depth-1, length/2)
        t.bk(length/2)
        t.lt(60)
        t.fd(length/2)
        t.rt(60)
        original_draw_sierpinski(t, depth-1, length/2)
        t.rt(120)
        t.fd(length/2)
        t.lt(120)

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

def original_tree(t, depth, length, angle):
    if(depth==1):
        t.fd(length)
        t.back(length)
    else:
        t.fd(length)
        t.lt(angle)
        original_tree(t, depth-1, length, angle)
        t.rt(2*angle)
        original_tree(t, depth-1, length, angle)
        t.lt(angle)
        t.bk(length)

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
        angle += random.randrange(-10, 10)
        t.fd(length)
        t.lt(angle)
        tree(t, depth-1, length*0.8, angle, width-1)
        t.rt(2*angle)
        tree(t, depth-1, length*0.8, angle, width-1)
        t.lt(angle)
        t.bk(length)

spike=turtle.Turtle()
turtle.colormode(255)

# spike.pu()
# spike.goto(-300, 0)
# spike.pd()
# draw_sierpinski(spike, 4, 300)

# spike.width(3)
# spike.pu()
# spike.goto(-300, 300)
# spike.pd()
# spike.lt(45)
# draw_koch(spike, 4, 15)

# spike.color(131, 67, 51)
# spike.lt(90)
# tree(spike, 10, 80, 20, 11)

original_draw_koch(spike, 4, 50)

window = turtle.Screen()
window.exitonclick()