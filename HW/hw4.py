'''
Abdulaziz
'''


def power_rec(a, b, total = 1):
    ''' tail recursive power function a^b  '''
    if b == 0:
        return total
    elif b < 0:
        return None
    else:
        total = total * a
        return power_rec(a, b - 1, total)


def power_rec_tail(a, b, total = 1 ):
    '''
    tail recursive power function a^b
    '''

    if b == 0:
        return total
    elif b<0:
        return None
    else:
        total = total *a
        return  power_rec(a, b - 1, total)


def power_iter(a, b):
    '''  same function with while loop a^b  '''
    total = 1
    while b > 0:
        total *= a
        b -= 1
    return total


def print_triangle(n):
    ''' funciton that draws a triangle tree with height of n like this:
    *
    **
    ***
    ****
    *****
    '''

    i = 1
    while i <= n:
        print("*" * i)
        i += 1


if __name__ == "__main__":
    #something
    pass

