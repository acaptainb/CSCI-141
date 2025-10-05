"""
Abdulaziz
CSCI-141
Tony Audi
Section 6
Group A
Probably Alison's group
Raindrops lab, 4
"""

import turtle as t
import random

Pond_SIZE = 700
Max_coordinates = Pond_SIZE//2
max_raindrop = 100
max_radius = 20
min_ripples = 2
max_ripples = 9

def pond():
    """
    Draws a filled square pond centered at (0,0).
    The pond is filled with aqua color and is of size Pond_SIZE.
    """
    t.penup()
    t.goto(-Pond_SIZE / 2, -Pond_SIZE / 2)
    t.pendown()
    t.setheading(0)
    t.fillcolor('aqua')
    t.begin_fill()
    t.forward(Pond_SIZE)
    t.left(90)
    t.forward(Pond_SIZE)
    t.left(90)
    t.forward(Pond_SIZE)
    t.left(90)
    t.forward(Pond_SIZE)
    t.left(90)
    t.end_fill()
    t.penup()
    t.goto(0, 0)

def draw_iter(n, r,c):
    """
    Draws a raindrop with n ripples.
    The first (center) circle is filled, rest are not.

    Returns total circumference of all ripple rings excluding center.
    """
    circle = 0
    rad =r
    first_circle = n
    while n >= 1:
        if n== first_circle:
            t.fillcolor(c)
            t.begin_fill()
            t.circle(rad)
            t.end_fill()
        else:
            t.circle(rad)
            circle+= 2 * 3.1415 * rad
        t.penup()
        t.right(90)
        t.forward(r)
        t.pendown()
        t.left(90)
        rad+=r
        n=n-1
    return circle

def Raindrop_radius():
    """
    Returns a random radius for a ripple circle.
    """
    return random.randint(1, max_radius)

def Raindrop_coordinates(r, n):
    """
    Generates random (x, y) coordinates for a raindrop in the pond, so
    there's enough space for n ripples of radius r.
    Returns tuple (x, y) coordinates for raindrop placement.
    """
    largest_radius = r * (n+1)
    x = random.randint(-Max_coordinates  + largest_radius, Max_coordinates  - largest_radius)
    y = random.randint(-Max_coordinates  + largest_radius, Max_coordinates  - largest_radius)
    return (x, y)

def setRandomColor():
    """
    Generates a random RGB color tuple for the raindrop center.
    Returns (r, g, b) with each value between 0 and 1.
    """
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def number_of_ripples():
    """
    Returns a random number of ripples for a raindrop.
    Range: min_ripples to max_ripples (inclusive).
    """
    return random.randint(min_ripples, max_ripples)

def ripple_inside_pond(x, y, r, n):
    """
    Checks if all ripples of a raindrop will fit in the pond.
    Returns True if all ripples stay within pond bounds, False otherwise.
    """
    largest_radius = r * n
    return (
        x - largest_radius >= -Max_coordinates and
        x + largest_radius <= Max_coordinates and
        y - largest_radius >= -Max_coordinates and
        y + largest_radius <= Max_coordinates
    )

def draw_raindrop():
    """
    Draws a single raindrop with a colored center and ripple rings,
    only if it fits within the pond.
    Returns the sum of total circumference of ripples (excluding center),
    or 0 if the drop was skipped.
    """
    r = Raindrop_radius()
    n= number_of_ripples()
    (x, y) = Raindrop_coordinates(r,n)
    if ripple_inside_pond(x, y, r, n ):
        t.penup()
        t.setpos(x, y )
        t.pendown()
        c=setRandomColor()
        t.begin_fill()
        ripple_circum = draw_iter(n, r,c)
        t.end_fill()
        t.penup()
        t.goto(0, 0)
        t.pendown()
        return ripple_circum
    else:
        return False

def main():
    """
    Asks user for number of raindrops.
    Draws the pond and the number of raindrops that user asked.
    Prints the total circumference of ripples and how many returned.
    """
    t.hideturtle()
    t.penup()
    t.goto(-Pond_SIZE / 2, Pond_SIZE / 2)
    t.pendown()

    n = int(input("Enter number of raindrops (1 - 100): "))
    if not (1 <= n <= max_raindrop):
        print("Number must be between 1 and 100.")
        return
    pond()
    i = 0
    total_circumference = 0
    while i < n:
        ripple_circum = draw_raindrop()
        total_circumference += ripple_circum
        i += 1

    print(n, " raindrops drawn inside the pond.")
    print("Total circumference of all ripples: ", total_circumference)
    t.done()

if __name__ == "__main__":
    t.speed(0)
    main()
