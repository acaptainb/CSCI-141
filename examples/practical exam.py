
"""
<Your Name Here>

Complete the two functions below. Each one is worth 50 points
See screenshot for correct output
See docstrings with each question for specific requirements
General algorithm for both functions:
    Determine which color to fill the shape with
    Draw the shape
    Calculate area and add to total
    Move turtle to start of next shape (with the pen up of course)
    Repeat smaller as necessary
    Return total Area
"""
import turtle
import turtle as t
import math

CIRCLE_COLOR_1 = 'red'
CIRCLE_COLOR_2 = 'yellow'

def recursive_circles(size:int, step:int, count:int, area = 0) -> int:
    """
    This function draws concentric circles with every other circle being a different color as defined above
        Size is the radius of the largest circle.
        Step is how much smaller each circle gets.
        Count is the number of circles
    This function should return the total area of all circles drawn
    For full credit this function must be written as a tail recursive function
    This means you will need to modify the function definition above
    Pre condition - turtle facing east, pen up
    Post condition - turtle facing east, pen up
    """
    if count%2 == 0:
        color = CIRCLE_COLOR_1
    else:
        color = CIRCLE_COLOR_2


    if count ==0:
        return area
    else:
            t.down()
            t.fillcolor(color)
            t.begin_fill()
            t.circle(size)
            t.end_fill()
            t.up()
            t.left(90)
            t.forward(step)
            t.right(90)
            return recursive_circles(size-step, step, count-1, area + math.pi *size**2)


SQUARE_COLOR_1 = 'blue'
SQUARE_COLOR_2 = 'green'

def iterative_squares(size:int, step:int, count:int) ->int:
    """
    This function draws concentric squares with every other square being a different color as defined above
        Size is the side length of the largest square.
        Step is how much smaller each square gets.
        Count is the number of squares
    This function should return the total area of all squares drawn
    For full credit this function must be written using iteration within iteration
    Pre condition - turtle facing east, pen up
    Post condition - turtle facing east, pen up
    """
    area = 0

    while count >= 0:
            t.down()

            if count % 2 == 0:
                t.fillcolor(SQUARE_COLOR_1)
            else:
                t.fillcolor(SQUARE_COLOR_2)

            t.begin_fill()
            for i in range(4):
                t.forward(size)
                t.left(90)
            t.end_fill()

            t.up()
            t.left(90)
            t.forward(step/2)
            t.right(90)
            t.forward(step/2)

            count-=1
            size-=step
            area += size * size
    return area
print(6//5)
def main():
    """
    The main functionm is set up to excercise the two functions above.
    If they are written correctly the output will match the associated screenshot
    """
    # Turn the tracer ON for testing

    t.tracer(False)

    # YOU SHOULD NOT NEED TO MODIFY ANYTHING BELOW

    XSPACING = 320
    YSPACING = 100
    t.setup(1400, 1000, 0, 0)
    t.speed(0)
    t.pencolor('black')
    t.pensize(2)
    t.up()
    sizes = [100,160,130,140]
    steps = [20,15,10,25]
    counts = [4,10,8,6]
    num = len(sizes)
    #  Draw circles and print areas
    for i in range(len(sizes)):
        t.goto(-(XSPACING * num //2 ) - XSPACING // 2 + (XSPACING * (i + 1)), YSPACING)
        area = recursive_circles(sizes[i]+10, steps[i], counts[i])
        t.goto(-(XSPACING * num //2 ) - XSPACING // 2 + (XSPACING * (i + 1)), YSPACING * 0.5)
        t.pendown()
        t.write(int(area), font=('Courier',20,'bold'), align='center')
        t.penup()

    #  Draw squares and print areas
    for i in range(len(sizes)):
        cur_size = sizes[i] * 1.5
        t.goto(-(XSPACING * num //2 ) - XSPACING // 2 - cur_size // 2 + (XSPACING * (i + 1)), -YSPACING * 3)
        area = iterative_squares(cur_size, steps[i] * 1.5, counts[i])
        t.goto(-(XSPACING * num //2 ) - XSPACING // 2 + (XSPACING * (i + 1)), -YSPACING * 3.5)
        t.pendown()
        t.write(int(area), font=('Courier',20,'bold'), align='center')
        t.penup()
    t.goto(0,0)
    t.tracer(True)
    t.done()

if __name__ == '__main__':
    main()
