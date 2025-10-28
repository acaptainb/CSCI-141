def collatz_steps(n, print_steps = True):
    if print_steps:
        print(n, end=' ')
    if n == 1:
        return 1
    elif n % 2 == 0:  # N is even
        return 1 + collatz_steps(n // 2, print_steps)
    else:             # N is odd
        return 1 + collatz_steps(3 * n + 1, print_steps)

def collatz_steps_tail(n, acc = 1):
    print(n, end=' ')
    if n == 1:
        return acc
    elif n % 2 == 0:  # N is even
        return collatz_steps_tail(n // 2, acc + 1)
    else:             # N is odd
        return collatz_steps_tail(3 * n + 1, acc + 1)

def collatz_steps_iter(n):
    steps = 1
    while n != 1:
        print(n, end = ' ')
        if n % 2 == 0:
            n = n // 2
            steps += 1
        else:
            n = 3 * n + 1
            steps += 1
    print(n, end = ' ')
    return steps

def main():
    n = int(input('Enter N: '))
    if n <= 0:
        print('N > 0')
    else:
        print('\ncollatz(', n, ')=', collatz_steps(n))
        print('\ncollatz tail(', n, ')=', collatz_steps_tail(n))
        print('\ncollatz iter(', n, ')=', collatz_steps_iter(n))


if __name__ == '__main__':
    main()