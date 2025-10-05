def square(x):
    return x*x

def collatz(x):
    return 1

def collatz2(x,acc=1):
    if x==1:
      print()
      return acc
    elif x%2==0:
      return collatz(x//2, acc+1)
    else:
      return collatz2(3*x+ 1 ,acc+1)