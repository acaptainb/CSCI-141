'''
Abdulaziz
'''

def is_between(a, b, c):
    if b <= c <= a or a <= c<= b:
        return True
    else:
        return False

def perform_op(op1, op2, operation):
    if operation not in ['+','-','*','/']:
        return None
    elif operation == '+':
        return op1 + op2
    elif operation == '-':
        return op1 - op2
    elif operation == '*':
        return op1 * op2
    elif operation == '/':
        if op2 == 0:
            return None
        return op1 / op2

def draw_shape(shape,size):
    if shape not in ['circle','triangle']:
        return None
    import turtle as t
    if shape == 'circle':
        t.circle(size)
    elif shape == 'triangle':
            t.forward(size)
            t.left(120)
            t.forward(size)
            t.left(120)
            t.forward(size)
            t.left(120)
    # t.done()

if __name__ == "__main__":
    # a, b, =map(int,input("put the number here").split())
    # x=int(input("put the number here: "))
    # c=input("put the shape here:")
    # print(is_between(a,b,c))
    # print(perform_op(a,b,c))
    # print(draw_shape(c,x))
    pass