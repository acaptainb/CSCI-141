import turtle


def draw1(sz):
    turtle.forward(2 * sz)
    turtle.back(2 * sz)
    turtle.circle(sz)

# draw1()
def draw2(sz):
    turtle.forward(2 * sz)
    draw1(sz / 2)
    turtle.back(2 * sz)
    turtle.circle(sz)


def draw3(sz):
    turtle.forward(2 * sz)
    draw2(sz / 2)
    turtle.back(2 * sz)
    turtle.circle(sz)


def draw(level, sz):
    #turtle goes forward and goes back by half size and draws a circle each time half the size of the last circle
    if level == 0:
        pass
    else:
        turtle.forward(2 * sz)
        draw( level - 1, sz/2)
        turtle.back(2 * sz)
        turtle.circle(sz)

def draw_color(level, sz, pc):
    #same draw function but each circle's pencolor changes from red to blue
    if level == 0:
        pass
    else:
        turtle.forward(2 * sz)
        draw_color( level - 1, sz/2, pc)
        if level%2 == 0:
            turtle.pencolor('red')
        else:
            turtle.pencolor('blue')
        turtle.back(2 * sz)
        turtle.circle(sz)



def compute(n, a):
    #recursion by given formula
    if n < 0:
        return 0
    if n < 2:
        return n
    else:
        return compute((n - 1),a) - compute((n - 2),a) * a


if __name__ == "__main__":
    draw_color(2, 100, 'blue')
    # draw(4, 50)
    turtle.done()
