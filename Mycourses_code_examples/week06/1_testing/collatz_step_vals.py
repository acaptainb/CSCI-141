def collatz_step_vals(n, acc = ""):
    if n == 1:
        return acc + "1"
    elif n % 2 == 0:  # N is even
        return collatz_step_vals(n // 2, acc + str(n) + "," )
    else:             # N is odd
        return collatz_step_vals(3 * n + 1, acc + str(n) + ",")

def main():
    n = int(input('Enter N: '))
    if n <= 0:
        print('N > 0')
    else:
        print('\ncollatz steps values (', n, ')=', collatz_step_vals(n))

if __name__ == '__main__':
    main()