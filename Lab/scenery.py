import turtle as t
import random


def draw_pine(height):
    '''

    :precondition:
    :postcondition:
    '''
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

    :precondition:
    :postcondition:
    '''
    t.left(90)
    t.forward(h)
    t.right(90)
    t.circle(h * 0.4)
    t.right(90)
    t.forward(h)
    t.left(90)


def draw_house(w, color):
    '''

    :precondition:
    :postcondition:
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
    t.pencolor('black')


tree1_height = random.randint(50, 200)
tree2_height = random.randint(50, 200)


def generate_tree1():
    '''

    '''
    trees1 = [draw_pine, draw_maple]
    tree1 = random.choice(trees1)
    tree1(tree1_height)
    return tree1


def generate_tree2():
    '''

    '''
    trees2 = [draw_pine, draw_maple]
    tree2 = random.choice(trees2)
    tree2(tree2_height)
    return tree2


def random_height():
    #
    return random.randint(50, 200)


def generate_maple():
    #
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

    :precondition:
    :postcondition:
    '''
    house = input("you want house? y/n ")
    if house == 'y':
        w = int(input("how big: "))
        colour = input('whats the color? ')
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
            print(tree1_height, tree2_height, tree3, (3 * w + (w * (2 ** (1 / 2)))))
            if tree1 == draw_pine:
                if tree2 == draw_pine:
                    print((2.8 * tree1_height) + (2.8 * tree2_height) + (0.8 * 3.14 * tree3) + (
                                500 + 3 * w + (w * (2 ** (1 / 2)))))
                elif tree2 == draw_maple:
                    print((2.8 * tree1_height) + (0.8 * 3.14 * tree2_height) + (0.8 * 3.14 * tree3) + (
                                500 + 3 * w + (w * (2 ** (1 / 2)))))
            elif tree1 == draw_maple:
                if tree2 == draw_pine:
                    print((0.8 * 3.14 * tree1_height) + (2.8 * tree2_height) + (0.8 * 3.14 * tree3) + (
                                500 + 3 * w + (w * (2 ** (1 / 2)))))
                elif tree2 == draw_maple:
                    print((0.8 * 3.14 * tree1_height) + (0.8 * 3.14 * tree2_height) + (0.8 * 3.14 * tree3) + (
                                500 + 3 * w + (w * (2 ** (1 / 2)))))
        else:
            print(tree1_height, tree2_height)
            if tree1 == draw_pine:
                if tree2 == draw_pine:
                    print((2.8 * tree1_height) + (2.8 * tree2_height) + (400 + 3 * w + (w * (2 ** (1 / 2)))))
                elif tree2 == draw_maple:
                    print((2.8 * tree1_height) + (0.8 * 3.14 * tree2_height) + (400 + 3 * w + (w * (2 ** (1 / 2)))))
            elif tree1 == draw_maple:
                if tree2 == draw_pine:
                    print((0.8 * 3.14 * tree1_height) + (2.8 * tree2_height) + (400 + 3 * w + (w * (2 ** (1 / 2)))))
                elif tree2 == draw_maple:
                    print((0.8 * 3.14 * tree1_height) + (0.8 * 3.14 * tree2_height) + (
                                400 + 3 * w + (w * (2 ** (1 / 2)))))

    else:
        t.setup(1300, 700)
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
                    print((2.8 * tree1_height) + (2.8 * tree2_height) + (0.8 * 3.14 * tree3) + (400))
                elif tree2 == draw_maple:
                    print((2.8 * tree1_height) + (0.8 * 3.14 * tree2_height) + (0.8 * 3.14 * tree3) + (400))
            elif tree1 == draw_maple:
                if tree2 == draw_pine:
                    print((0.8 * 3.14 * tree1_height) + (2.8 * tree2_height) + (0.8 * 3.14 * tree3) + (400))
                elif tree2 == draw_maple:
                    print((0.8 * 3.14 * tree1_height) + (0.8 * 3.14 * tree2_height) + (0.8 * 3.14 * tree3) + (400))
        else:
            print(tree1_height, tree2_height)
            if tree1 == draw_pine:
                if tree2 == draw_pine:
                    print((2.8 * tree1_height) + (2.8 * tree2_height) + (300))
                elif tree2 == draw_maple:
                    print((2.8 * tree1_height) + (0.8 * 3.14 * tree2_height) + (300))
            elif tree1 == draw_maple:
                if tree2 == draw_pine:
                    print((0.8 * 3.14 * tree1_height) + (2.8 * tree2_height) + (300))
                elif tree2 == draw_maple:
                    print((0.8 * 3.14 * tree1_height) + (0.8 * 3.14 * tree2_height) + (300))


main()
t.done()