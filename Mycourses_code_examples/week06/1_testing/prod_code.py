def add_nums(a:int, b:int)->int:
    return a + b

def collatz(n:int)->int:
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz(n // 2)
    else:
        return collatz((3 * n) + 1)

def collatz_steps(n:int, acc:int=1)->int:
    if n == 1:
        return acc
    elif n % 2 == 0:
        acc += 1
        n = n // 2
        return collatz_steps(n, acc)
    else:
        acc += 1
        n = (3 * n) + 1
        return collatz_steps(n, acc)


def main():
    print(add_nums(1, 2))
    print(add_nums(5, 6))

if __name__ == "__main__":
    main()