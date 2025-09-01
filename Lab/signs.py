import turtle as t



def diamond_sign():
    '''

    :return:
    '''
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
# diamond_sign()
def sign():
    '''

    :return:
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

    :return:
    '''
    t.right(90)
    t.forward(60)
    t.up()
    t.left(180)
    t.forward(195)


def own_sign():

    t.forward(50)
    t.down()
    sign()
    t.up()
    t.left(90)
    t.forward(80)
    t.left(180)
    t.down()
    t.forward(160)


sign()
sign1()
own_sign()
t.done()