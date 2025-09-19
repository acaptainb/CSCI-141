import turtle
import random
import math

def draw_square(leght):
    turtle.begin_fill()
    turtle.forward(leght)
    turtle.left(90)
    turtle.forward(leght)
    turtle.left(90)
    turtle.forward(leght)
    turtle.left(90)
    turtle.forward(leght)
    turtle.left(90)
    turtle.end_fill()




def rec_squares(lenght:float)->None:
    if lenght<5:
        return None
    else:
        draw_square(lenght)
        area = lenght*lenght

        half = lenght/2
        turtle.forward(half)
        turtle.left(45)
        next_val = math.sqrt(half**2*2)
        total = area + rec_squares(next_val)
        return total


def squares(lenght:float)->None:
    area = 0
    # while lenght>=5:

    return area





def main():
    turtle.speed(0)
    rec_squares(200)
main()