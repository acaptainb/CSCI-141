"""
CSCI-141 Computer Science 1 Recitation Exercise
03-Recursion
Shapes

Here is where you write a general recursive solution to the drawing
problem by implementing draw_shapes.
"""

import turtle

def init(depth):
    """
    Write the depth and set up the turtle so it is at the initial state.
    :param depth: the detail of the shape to draw
    :pre turtle is at the center, down and facing east
    :post turtle is at the center, down and facing east
    """
    turtle.pensize(4)
    turtle.speed(0)
    turtle.up()
    turtle.backward(200)
    turtle.write('Depth: ' + str(depth), font = ("Arial", 24, "bold"))
    turtle.forward(200)
    turtle.down()

def set_color(depth):
    """
    Change the color of what the turtle draws based on the depth.
    :param depth: the detail of the shape to draw
    """
    if depth == 1:
        turtle.color('green')
    elif depth == 2:
        turtle.color('blue')
    elif depth == 3:
        turtle.color('red')
    elif depth == 4:
        turtle.color('purple')
    else:
        turtle.color('black')

def draw_shapes(length, depth):
    """
    Draw the shape at the current depth of detail.
    :param length: length of the segments
    :param depth: the current level of detail we are at
    :pre turtle is at the center, down and facing east
    :post turtle is at the center, down and facing east
    """
    # IMPLEMENT YOUR SOLUTION HERE
    if depth == 1:
        set_color(depth)
        turtle.circle(length/2)
    else:
        set_color(depth)
        turtle.forward(length)
        draw_shapes(length/2, depth-1)
        turtle.left(120)
        set_color(4)
        # turtle.circle(length)
        turtle.forward(length)
        draw_shapes(length/2, depth-1)
        turtle.left(120)
        set_color(3)
        turtle.forward(length)
        draw_shapes(length/2, depth-1)
        turtle.left(120)

def draw_polygon(sides, length):
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360/sides)

def draw_shapesss(length, depth):
    if depth == 1:
        set_color(depth)
        draw_polygon(6, length/3)   # base case = hexagon
    else:
        for _ in range(3):          # 3 sides = triangle
            set_color(depth)
            turtle.forward(length)
            draw_shapes(length/2, depth-1)   # put a smaller triangle at this corner
            turtle.left(120)
draw_polygon(6, 100)

def main():
    """
    The main program prompts for the depth and then calls the recursive
    drawing function, draw_shapes, to draw the complete image.
    """
    depth = int(input('Enter depth: '))
    # init(depth)
    turtle.tracer(0,0)
    # draw_shapesss(200, depth)
    turtle.done()

if __name__ == '__main__':
    main()