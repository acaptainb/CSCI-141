import turtle as t

def draw_polygon(side, sides, len):
    while side <=sides:
        t.forward(len)
        t.left(360/sides)
        side = side + 1
# draw_polygon(1,5,100)


n=0
while n<11:
    n=n+1
    if n%2!=0:
        continue
    print(n)
print("done",n)