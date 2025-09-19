import turtle as t

pond_s=300

def pond():
    t.fillcolor('blue')
    t.begin_fill()
    t.forward(pond_s)
    t.left(90)
    t.forward(pond_s)
    t.left(90)
    t.forward(pond_s)
    t.left(90)
    t.forward(pond_s)
    t.back(pond_s/2)
    t.left(90)
    t.penup()
    t.forward(pond_s/2)
    t.end_fill()

def draw_iter(n, r):
    circle = 0
    rad =r
    while n >=1:
        # t.fillcolor("red")
        # t.begin_fill()
        t.circle(rad)
        # t.end_fill()

        t.penup()
        t.right(90)
        t.forward(r)
        t.pendown()
        t.left(90)
        circle+= 2 * 3.1415 * rad
        rad+=r
        n=n-1
    return circle
t.speed(0)
pond()
draw_iter(10, 5)
t.done()