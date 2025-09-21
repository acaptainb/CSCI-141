import turtle as t
import random
import math

# from examples.raindrops import BOX_SIZE

pensize = 1
Pond_SIZE = 340
Max_coordinates = Pond_SIZE/2
max_raindrop = 100
max_radius = 20
min_ripples = 3
max_ripples = 8


def pond():
    t.fillcolor('blue')
    t.begin_fill()
    t.forward(Pond_SIZE)
    t.left(90)
    t.forward(Pond_SIZE)
    t.left(90)
    t.forward(Pond_SIZE)
    t.left(90)
    t.forward(Pond_SIZE)
    t.back(Pond_SIZE /2)
    t.left(90)
    t.penup()
    t.forward(Pond_SIZE /2)
    t.end_fill()

def draw_iter(n, r):
    circle = 0
    rad =r
    first_circle = n
    while n >= 1:
        if n== first_circle:
            t.fillcolor("red")
            t.begin_fill()
            t.circle(rad)
            t.end_fill()
        else:
            t.circle(rad)
        t.penup()
        t.right(90)
        t.forward(r)
        t.pendown()
        t.left(90)
        circle+= 2 * 3.1415 * rad
        rad+=r
        n=n-1
    return circle
t.hideturtle()
t.speed(0)
pond()
draw_iter(10, 5)
t.done()