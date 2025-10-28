def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz(n // 2)
    else:
        return collatz(3 * n + 1)

def main():
    n = int(input("Enter a number: "))
    if n <= 0:
        print("N must be > 0")
    else:
        print("Collatze for ", n, " = ", collatz(n))

if __name__ == '__main__':
    main()