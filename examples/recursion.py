import turtle


def print_nums_rec(current:int, finish:int)-> None:
    if current == finish:
        print(current)
    else:
        # print(current)
        next_val = current +1 # get ready for next step
        print_nums_rec(next_val, finish) # recursion
        print(current) # do the work

def print_nums_rec_total(current:int, finish:int)-> int:
    if current == finish:
        # print(current)
        return current
    else:
        # print(current)
        next_val = current +1 # get ready for next step
        total = current + print_nums_rec_total(next_val, finish) # recursion
        return total


def main():
    total = print_nums_rec_total(1, 10)
    print(total)
    # print_nums_rec(1, 10)


def factorial(n: int)->int:
    if n<0:
        return None
    elif n==0  or n==1:
        return 1
    else:
        next_val = n-1
        fact_rest = factorial(next_val)
        return n*fact_rest



def fib(n: int)->int:
    if n<0:
        return None
    elif n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def gcd(m: int, n:int)->int:
    if m%n ==0:
        return n
    else:
        return gcd(n, m%n)

gcd(12,90)





import turtle as t





def draw_tree_0(size:int)-> None:
    pass
def draw_tree_1(size:int)-> None:
    t.forward(size)
    t.forward(-size)
    draw_tree_0((size))

def draw_tree_2(size:int)-> None:
    t.forward(size)
    t.left(45)
    draw_tree_1((size//2))
    t.right(90)
    draw_tree_1((size//2))
    t.left(45)
    t.forward(-size)


def draw_tree_3(size: int) -> None:
    t.forward(size)
    t.left(45)
    draw_tree_2((size // 2))
    t.right(90)
    draw_tree_2((size // 2))
    t.left(45)
    t.forward(-size)

def draw_tree_rec(size: int, depth: int) -> None:
    if depth==0:
        pass
    else:
        t.forward(size)
        t.left(45)
        draw_tree_rec((size // 2, depth-1))
        t.right(90)
        draw_tree_rec((size // 2, depth-1))
        t.left(45)
        t.forward(-size)

def blastoff( countdown):
    if countdown==0:
        pass
    else:
        print(countdown)
        blastoff(countdown-1)
        # blastoff(10)


# blastoff(10)
# print('blastoff!')
if __name__ == '__main__':
    # print(fib(20))
    # print(factorial(10))
    # main()
    #  print(gcd(20, 90))
    # t.speed(0)
    # t.tracer(False)
    # draw_tree_rec(100,5)
    gcd(12,90)

    # t.done()