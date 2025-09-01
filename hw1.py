'''
Abdulaziz
'''
import turtle
def hello():
    print('Welcome to CS1 @ RIT!')
    pass
hello()
def draw_triangle():
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(200)
    pass
# draw_triangle()
def draw_hazard():
    turtle.left(120)
    draw_triangle()
    turtle.left(120)
    draw_triangle()
    turtle.left(120)
    draw_triangle()
    pass
# draw_hazard()
if __name__ == "__main__":
    # you can put code here to run your functions for testing
    # do not add extra code outside here or the functions you
    # are writing or it may confuse/break the autograder
    pass
# turtle.done()
