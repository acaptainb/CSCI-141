import turtle as t
import random


# pensize = 1
Pond_SIZE = 700
Max_coordinates = Pond_SIZE//2
max_raindrop = 100
max_radius = 20
min_ripples = 2
max_ripples = 9

def pond():
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
        t.penup()
        t.right(90)
        t.forward(r)
        t.pendown()
        t.left(90)
        circle+= 2 * 3.1415 * rad
        rad+=r
        n=n-1
    return circle

def Raindrop_radius():
    return random.randint(1, max_radius)

def Raindrop_coordinates(r, n):
    largest_radius = r * (n+1)
    x = random.randint(-Max_coordinates  + largest_radius, Max_coordinates  - largest_radius)
    y = random.randint(-Max_coordinates  + largest_radius, Max_coordinates  - largest_radius)
    return (x, y)

def setRandomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

def number_of_ripples():
    return random.randint(min_ripples, max_ripples)


def ripple_inside_pond(x, y, r, n):
    largest_radius = r * (n+1)
    return (
        x - largest_radius >= -Max_coordinates and
        x + largest_radius <= Max_coordinates and
        y - largest_radius >= -Max_coordinates and
        y + largest_radius <= Max_coordinates
    )

def draw_raindrop():
    r = Raindrop_radius()
    n= number_of_ripples()
    (x, y) = Raindrop_coordinates(r,n)
    if ripple_inside_pond(x, y, r, n ):
        t.penup()
        t.setpos(x, y )
        t.pendown()
        c=setRandomColor()
        t.begin_fill()
        draw_iter(number_of_ripples(), r,c)
        t.end_fill()
        t.penup()
        t.goto(0, 0)
        t.pendown()
        return True
    else:
        return False


def main():
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
    while i < n:
        draw_raindrop()
        i += 1

    print(f"{n} raindrops drawn inside the pond.")
    t.done()


if __name__ == "__main__":
    t.speed(0)
    main()

