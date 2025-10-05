import math
# a='hello'
# print(len(a))
# for i in a:
#     b=bin(ord(i))
#     print(b)
x, y = input().split()
x2 = int(x[1])
x1 = ord(x[0]) - 96
y2 = int(y[1])
y1 = ord(y[0]) - 96
dist = math.sqrt((y1 - x1) ** 2 + (y2 - x2) ** 2)
target = math.sqrt(2) / 2
print(math.ceil(target))

