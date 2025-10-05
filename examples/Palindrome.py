import turtle as t

def draw_iter(n, r,c):
    """
    Draws a raindrop with n ripples.
    The first (center) circle is filled, rest are not.

    Returns total circumference of all ripple rings excluding center.
    """
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
            circle+= 2 * 3.1415 * rad
        t.penup()
        t.right(90)
        t.forward(r)
        t.pendown()
        t.left(90)
        rad+=r
        n=n-1
    return circle

def draw_hex(n, l,c):
    """
    Draws a raindrop with n ripples.
    The first (center) circle is filled, rest are not.

    Returns total circumference of all ripple rings excluding center.
    """
    hex= 0
    lenght=l
    first_hex = n
    while n >= 1:
        if n== first_hex:
            t.fillcolor(c)
            t.begin_fill()
            for i in range(6):
                t.forward(lenght)
                t.right(60)
            t.end_fill()
        else:
            # t.circle(lenght)
            for i in range(6):
                t.forward(lenght/3)
                t.right(60)
            hex+= 2 * 3.1415 * lenght
        t.penup()
        t.right(90)
        t.forward(l)
        t.pendown()
        t.left(90)
        lenght+=l
        n=n-1
    return hex

hex=draw_hex(2,50,"red")
print(hex)

# def main():
#     draw_iter(3,10,"blue")


# if __name__ == '__main__':
    # main()