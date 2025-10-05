def divider(x,y):
    value =23
    if y!=0:
        print('error: devide by zero')
    else:
        print('divide by zero')

def hanoi(n):
    if n==1:
        return 1
    else:
        return 2* hanoi(n-1) +1

print(hanoi(4))

# luck='G o o d  L u c k !’
# walk='Walk in the Park’
x = 4
y = 9

#
#  l u c k [ 8 ]
# K
#  l u c k [ x + 6 ]
# error
# len ( l u c k )
# 10
# l u c k [ y ]
# !
# l u c k [ =1]
# !
# len ( walk )
# 16
# walk=[len(walk)]
# error
# luck[:3]
# GOO
# # l u c k [ 5 : ]
# UCK
# l u c k [ 6 : y ]
# CK!
# l u c k [ 3 : 3 ]
#
# walk [ : : 2 ]
# Wi ntePr
# l u c k [ : : 1 ]
# !kcuL dooG
#  l u c k [ -2: 2]
#   (end is greater than start)
# l u c k [ -5: -2]
# Luc