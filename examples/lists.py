# a=[]
# print(a)

# b=list(range(1,10))
# print(b)
# for v in b:
#     a.append(v)
# print(a)
# # a[0]=None
# print(a, end="| \n")
# for i in range(len(a)):
#     a[i]= a[i]**2
# print(a)
# print(36 in a)
# b=a+(a[3:])
# print(b)
# print(a)
# for i in range(len(b)):
#     print(b[i] ,end="| \n")
# list=[]
# for i in range(10):
#     list.insert(0,i)
# print(list)

# lista=['Herm']
# listb=['ionoe']
# lista+=listb
# print(lista)
# print(listb)

# str = 'this is split string'
# lstd = str.split()
# print(lstd)
# for s in lstd:
#     print(s)


# comp1=[x**2 for x in range(1,10) if x%2==0]
# tup = tuple(comp1)
# print(comp1)
# print(tup)

# for i in tup:
#     print(i)
# for i in range(len(tup)):
#     print(i*'8')
#     print(tup[i])



size =5
table =[]
for i in range(size):
    row=[]
    for j in range(size):
        row.append(i*j)
    table.append(row)
for row in table:
    print(row)

# table = [[i*j for j in range(size)] for i in range(size)]
#
# for row in table:
#     print(row)


def merge_sort(n):
    if n==1:
        return n

    # m = n//2
    # l = [m:]
    # r = [:m]



