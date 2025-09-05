import turtle as t

t.setup(1500, 400)

def diamond_sign():
    '''
    draws the shape of a sign with color and border with size 3 pen.
    :precondition:Turtle's pen is up.
    :postcontion: Turtle's state is the same as at start of the function.
    '''
    t.down()
    t.pencolor('black')
    t.pensize(3)
    t.fillcolor("yellow")
    t.begin_fill()
    t.left(45)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(200)
    t.right(135)
    t.end_fill()
    t.up()
def sign():
    '''
    draws the straight line inside the sign for as base function for reusing ir for other signs.
    :precondition: Turtle's pen is up.
    :postcontion:Turtle facing north in the middle of the straight line.
    '''
    diamond_sign()
    t.pensize(18)
    t.forward(140)
    t.left(90)
    t.forward(70)
    t.left(180)
    t.down()
    t.forward(160)
    t.right(180)
    t.forward(85)


def sign1():
    '''
    A road sign indicating side road on the right;
     :precondition: Turtle's pen is up.
     :postcontion: turtle's state is at the end of the line.
    '''
    t.down()
    sign()
    t.down()
    t.right(90)
    t.forward(60)
    t.up()

def own_sign():
    '''
    turtle draws a cross road.
    :precondition: Turtle's pen is up.
    :postcontion:turtle's state is at the end of the line.
    '''
    t.forward(50)
    t.down()
    sign()
    t.up()
    t.left(90)
    t.forward(80)
    t.left(180)
    t.down()
    t.forward(160)
    t.up()
def sign2():
    '''
    A road sign indicating side road on the left;
    :precondition:Turtle's pen is up.
    :postcontion: Turtle's state is the in the middle of the sign facing west.
    '''
    t.down()
    sign()
    t.right(90)
    t.forward(60)
    t.back(60)
    t.left(180)
    t.up()

def sign3():
    '''
    A road sign indicating ‘T’ intersection;
    :precondition:Turtle's pen is up.
    '''
    t.down()
    sign()
    t.forward(75)
    t.left(90)
    t.back(50)
    t.forward(100)
    t.up()
def main():
    '''
    First set the speed at 0. then draws the Sign1 then, go the left and draws the cross road sign,
     the to the left for Sign2 then to the right past 2 other signs then draws Sign3
    '''
    t.speed(0)
    sign1()
    t.left(180)
    t.forward(195)
    own_sign()
    t.forward(90)
    sign2()
    t.forward(820)
    sign3()
main()
t.done()