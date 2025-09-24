import turtle as t
import random


def draw_pine(height):
    '''
    Draws a simple pine tree shape with a trunk and a triangle on top.

    :precondition: Turtle should be at the start position, facing right., starts with green ink
    :postcondition: Turtle ends at the same position, facing right.
   '''
    t.pencolor('green')
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(height * 0.3)
    t.left(120)
    t.forward(height * 0.6)
    t.left(120)
    t.forward(height * 0.6)
    t.left(120)
    t.forward(height * 0.3)
    t.right(90)
    t.forward(height)
    t.left(90)


def draw_maple(h):
    '''
    Draws a simple maple tree shape with a trunk and a 40% trunk height circle on top.

    :precondition: Turtle should be at the start position, facing right.starts with green ink
    :postcondition: Turtle ends at the same position, facing right.
    '''
    t.pencolor('green')
    t.left(90)
    t.forward(h)
    t.right(90)
    t.circle(h * 0.4)
    t.right(90)
    t.forward(h)
    t.left(90)


def draw_house(w, color):
    '''
    Draws a house with given width and color.

    :precondition: Turtle should be at the start position, facing right. first change the pencolor to users choice
    :postcondition: Turtle ends at the bottom end of the house, facing right. ends with green ink
    '''
    t.pencolor(color)
    t.left(90)
    t.forward(w)
    t.right(45)
    t.forward(w / (2 ** (1 / 2)))
    t.right(90)
    t.forward(w / (2 ** (1 / 2)))
    t.right(45)
    t.forward(w)
    t.left(90)
    t.backward(w)
    t.forward(w)
    t.pencolor('green')


tree1_height = random.randint(50, 200)
tree2_height = random.randint(50, 200)


def generate_tree1():
    '''
    Randomly draws either a pine or maple tree.
    '''
    trees1 = [draw_pine, draw_maple]
    tree1 = random.choice(trees1)
    tree1(tree1_height)
    return tree1


def generate_tree2():
    '''
    Randomly draws either a pine or maple tree.
    '''
    trees2 = [draw_pine, draw_maple]
    tree2 = random.choice(trees2)
    tree2(tree2_height)
    return tree2


def random_height():
    # Picks a random number between 50 and 200 to use as a height.
    return random.randint(50, 200)


def generate_maple():
    # Randomly decides to draw a maple tree or skip.
    # If drawn, it picks a random height, draws the tree, and moves the turtle forward.
    maple = [True, False]
    r = random.choice(maple)
    if r is True:
        tree3_height = random_height()
        draw_maple(tree3_height)
        t.forward(100)
        return tree3_height
    else:
        pass


def main():
    '''
    Asks the user if they want a house, its size, and color.
    Draws a scene with random trees, a house (if chosen), and another random tree.
    Then attempts to draw an optional maple tree.
    Finally, calculates and prints the total ink used for all drawn objects.
    '''
    house = input("you want house? y/n ")
    if house == 'y':
        w = int(input("how big: "))
        colour = input('whats the color? ')
        t.pencolor('green')
        t.setup(1500, 800)
        # t.speed(0)

        t.backward(200)
        t.forward(100)
        tree1 = generate_tree1()
        t.forward(100)
        draw_house(w, colour)
        t.forward(100)
        tree2 = generate_tree2()
        t.forward(100)
        tree3 = generate_maple()
        if tree3 is not None:
            # print(tree1_height, tree2_height, tree3, (3 * w + (w * (2 ** (1 / 2)))))
            if tree1 == draw_pine:
                if tree2 == draw_pine:
                    print((2.8 * tree1_height) + (2.8 * tree2_height) + (0.8 * 3.14 * tree3) + (
                                500 + 3 * w + (w * (2 ** (1 / 2)))), " ink used")
                elif tree2 == draw_maple:
                    print((2.8 * tree1_height) + (0.8 * 3.14 * tree2_height) + (0.8 * 3.14 * tree3) + (
                                500 + 3 * w + (w * (2 ** (1 / 2))))," ink used")
            elif tree1 == draw_maple:
                if tree2 == draw_pine:
                    print((0.8 * 3.14 * tree1_height) + (2.8 * tree2_height) + (0.8 * 3.14 * tree3) + (
                                500 + 3 * w + (w * (2 ** (1 / 2))))," ink used")
                elif tree2 == draw_maple:
                    print((0.8 * 3.14 * tree1_height) + (0.8 * 3.14 * tree2_height) + (0.8 * 3.14 * tree3) + (
                                500 + 3 * w + (w * (2 ** (1 / 2))))," ink used")
        else:
            print(tree1_height, tree2_height)
            if tree1 == draw_pine:
                if tree2 == draw_pine:
                    print((2.8 * tree1_height) + (2.8 * tree2_height) + (400 + 3 * w + (w * (2 ** (1 / 2))))," ink used")
                elif tree2 == draw_maple:
                    print((2.8 * tree1_height) + (0.8 * 3.14 * tree2_height) + (400 + 3 * w + (w * (2 ** (1 / 2))))," ink used")
            elif tree1 == draw_maple:
                if tree2 == draw_pine:
                    print((0.8 * 3.14 * tree1_height) + (2.8 * tree2_height) + (400 + 3 * w + (w * (2 ** (1 / 2))))," ink used")
                elif tree2 == draw_maple:
                    print((0.8 * 3.14 * tree1_height) + (0.8 * 3.14 * tree2_height) + (
                                400 + 3 * w + (w * (2 ** (1 / 2))))," ink used")

    else:
        t.setup(1300, 700)
        t.pencolor('green')
        t.backward(200)
        t.forward(100)
        tree1 = generate_tree1()
        t.forward(100)
        tree2 = generate_tree2()
        t.forward(100)
        tree3 = generate_maple()
        if tree3 is not None:
            print(tree1_height, tree2_height, tree3, )
            if tree1 == draw_pine:
                if tree2 == draw_pine:
                    print((2.8 * tree1_height) + (2.8 * tree2_height) + (0.8 * 3.14 * tree3) + (400)," ink used")
                elif tree2 == draw_maple:
                    print((2.8 * tree1_height) + (0.8 * 3.14 * tree2_height) + (0.8 * 3.14 * tree3) + (400)," ink used")
            elif tree1 == draw_maple:
                if tree2 == draw_pine:
                    print((0.8 * 3.14 * tree1_height) + (2.8 * tree2_height) + (0.8 * 3.14 * tree3) + (400)," ink used")
                elif tree2 == draw_maple:
                    print((0.8 * 3.14 * tree1_height) + (0.8 * 3.14 * tree2_height) + (0.8 * 3.14 * tree3) + (400)," ink used")
        else:
            print(tree1_height, tree2_height)
            if tree1 == draw_pine:
                if tree2 == draw_pine:
                    print((2.8 * tree1_height) + (2.8 * tree2_height) + (300)," ink used")
                elif tree2 == draw_maple:
                    print((2.8 * tree1_height) + (0.8 * 3.14 * tree2_height) + (300)," ink used")
            elif tree1 == draw_maple:
                if tree2 == draw_pine:
                    print((0.8 * 3.14 * tree1_height) + (2.8 * tree2_height) + (300)," ink used")
                elif tree2 == draw_maple:
                    print((0.8 * 3.14 * tree1_height) + (0.8 * 3.14 * tree2_height) + (300)," ink used")

main()
t.done()