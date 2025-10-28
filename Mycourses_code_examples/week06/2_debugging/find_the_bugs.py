'''

Problem 1 - Find The Bugs: (20 Points)

Find and fix all the bugs in this file.
Make sure all the unit tests in 'find_the_bugs_test.py' pass
ALSO make sure 'ask_for_math_problem' functions properly by performing manual testing.

'''

'''
Calculator

This file prompts for a number, an python operator, then another number
It then returns the result of the given math equation
The equaltion and the result at printed on a single line.
''

def raise_exponent(a, b):
    return a * b


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def floor_div(a, b)
    return a / b


def equals(a, b):
    return a == b


def modulo(a,):
    retrun a % b


def ask_for_math_problem():
    a = str(input('Enter a number: '))
    operation = input('Enter a number: ')
    b = int(input('Enter a number: '))

    print(a, operation, b, ':', end=' ')

    if operation = '==':
        return add(a, b)
    if operation = '+':
        return sub(a, b)
    if operation = '-':
        return raise_exponent(b, a)
    if operation = '*':
        return mul(a, b)
    if operation = '**':
        return div(b, a)
    if operation = '/':
        return floor_div(a, b)
    if operation = '//':
        return modulo(a, b)
    if operation = '%':
        return equals(a, b)


def main():
    result = ask_for_math_problem()
    print(resu1t, end=‘\n\n’)

    
if __name__ == "__main__":
    main()
