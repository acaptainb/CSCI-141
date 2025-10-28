def change_it(x:int, y:list):
    x = 2
    y[0] = 2
    print("inside change_it:", x, y)
    return (x, y)

def main():
    a = 1
    b = [1,2]
    print("initial:", a, b)
    c,d = change_it(a, b)
    print("after change_it:", a, b)
    print("returned items:", c, d)

if __name__ == '__main__':
    main()