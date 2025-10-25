'''
A program that solves Laser Towers puzzles.
Instructor: Tony Audi
Author: Abdulaziz
'''
import sys

def read_num(path):
    """Reads string from a file and returns them as a integer list."""
    with open(path) as s:
        return [int(x) for x in s.read().split()]


def tower_placement(l):
    """Returns tuple for  all valid lasers for each index depending on up or down value for the given list.
    first if statement checks for every value excepts first and last 2.
    elif statement checks for first and last one.
    """
    possible = []
    for i in range(1,len(l)-1):
        if i + 2 < len(l) and i >= 2:
            up = l[i - 1] + l[i + 1] + l[i + 2]
            down = l[i - 1] + l[i + 1] + l[i - 2]
            if up > down:
                possible.append((i, "up", up))
            else:
                possible.append((i, "down", down))

        elif i + 2 < len(l):
            up = l[i - 1] + l[i + 1] + l[i + 2]
            possible.append((i, "up", up))

        elif i - 2 >= 0:
            down = l[i - 1] + l[i + 1] + l[i - 2]
            possible.append((i, "down", down))
    return possible


def quick_sort(arr):
    """ quick sort a list of towers in descending order by their sum."""
    n = len(arr)
    if n <= 1:
        return arr
    p = arr[-1]
    p_sum= p[2]
    L = [x for x in arr[:-1] if x[2] > p_sum]
    R = [x for x in arr[:-1] if x[2] <= p_sum]
    return  quick_sort(L) + [p] + quick_sort(R)

def main():
    """check the input by users, Reads the file from terminal, computes all tower placements, sorts them,
    and prints the top results."""
    if len(sys.argv) != 3:
        print("Usage: lasers.py laser-file num-towers")
        return
    filename = sys.argv[1]
    num_towers = int(sys.argv[2])
    read = read_num(filename)
    possible_towers = tower_placement(read)
    sorted_towers = quick_sort(possible_towers)
    best_towers = sorted_towers[:num_towers]
    print(read)
    print(num_towers, "\n")
    for i, j, z in best_towers:
        print("Centered at location", i,"facing", j,"scoring",z)

if __name__ == "__main__":
    main()


