"""
Abdulaziz Abbasov
"""
import turtle as t

def present(depth,length):
    """
     Draws a recursive present with depth
    squares are filled with green color and larger squares pensize will change with depth
    Precondition: Turtle is facing east with pen down
    Postcondition: Turtle is facing east with pen down
    """
    if depth == 0:
        return
    else:
        t.fillcolor('green')
        t.begin_fill()

        t.speed(0)
        present(depth-1,length*0.4)
        t.pensize(depth)
        t.forward(length)
        t.left(90)

        present(depth-1,length*0.4)
        t.pensize(depth)
        t.forward(length)
        t.left(90)

        present(depth-1,length*0.4)
        t.pensize(depth)
        t.forward(length)
        t.left(90)

        present(depth-1,length*0.4)
        t.pensize(depth)
        t.forward(length)
        t.left(90)

        t.end_fill()

def bow(depth,length):
    """
    Draws a recursive bow circles
    circles are filled with red color
    Precondition: Turtle is facing east with pen down
    Postcondition: Turtle is facing east.
    """
    if depth == 0:
        t.pensize(1)
        t.fillcolor('red')
        t.begin_fill()
        t.pendown()
        t.circle(length*3)
        t.end_fill()
    elif depth > 0:
        t.left(90)
        t.penup()
        t.forward(length)
        t.forward(length)
        bow(depth-1,length*1/3)
        t.penup()
        t.back(length)
        t.left(120)

        t.forward(length)
        bow(depth - 1, length*1/ 3)
        t.penup()
        t.back(length)
        t.left(120)

        t.forward(length)
        bow(depth - 1, length * 1 / 3)
        t.penup()
        t.back(length)
        t.left(120)

        t.back(length)
        t.right(90)

def main():
    """
    Main function that asks for user input about size and depth of the present and draws the present
    If user wants a bow, it asks for bow size and depth and draws it
    Precondition: No turtle window is open yet
    Postcondition: Turtle window remains open after drawing and turtle facing east with pen down.
    """
    global bow_depth
    present_depth = int(input("depth of present you want? "))
    present_size = int(input("How big a present you want? "))
    bow_y = input("you want a bow (y/n)? ")

    if bow_y == 'y':
        bow_size = int(input("size of bow? "))
        bow_depth = int(input("depth of bow? "))


    t.speed(0)
    t.penup()
    t.pendown()

    present(present_depth, present_size)

    if bow_y == 'y':
        t.penup()
        t.forward(present_size/2)
        t.left(90)
        t.forward(present_size/2 - bow_size)
        t.right(90)
        bow(bow_depth, bow_size)

if __name__ == '__main__':
    main()
    t.done()