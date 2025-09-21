import turtle as t

def draw_polygon(side, sides, len):
    while side <=sides:
        t.forward(len)
        t.left(360/sides)
        side = side + 1
# draw_polygon(1,5,100)


n=0
while n<7:
    n=n-2
    if n%2!=0:
        continue
    print(n)
print("done",n)




def drawsquare_iter(sides):
    while sides>0:
        t.forward(100)
        t.left(90)
        sides = sides - 1
        # drawsquarerec(sides-1)
# drawsquare_iter(4)



def fib(n, a=0, b=1):
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return fib(n-1, b, a+b)

# print(fib(50))