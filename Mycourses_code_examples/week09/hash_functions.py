import os
import time

current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/data/alice.txt"
RUNS = 100

def worst_hash_ever(a_string):
    '''
    :param a_string: the string to hash
    :return: the hash value
    The world's worst hash function.  Simply return 1 for every hash code
    '''
    return 1

def str_hash_1(a_string):
    '''
    :param a_string: the string to hash
    :return: the hash value
    A simple hash function which simply uses the maximum ascill value for the hash code
    '''
    max_ascii = -1
    for char in a_string:
        char_ascii = ord(char)
        if char_ascii > max_ascii:
            max_ascii = char_ascii
    return max_ascii


def str_hash_2(a_string):
    '''
    :param a_string: the string to hash
    :return: the hash value
    A slightly better hash function which takes the max ascii and multiplies it by the length of the string
    '''
    max_ascii = -1
    for char in a_string:
        char_ascii = ord(char)
        if char_ascii > max_ascii:
            max_ascii = char_ascii
    return max_ascii * len(a_string)


def str_hash_3(a_string):
    '''
    :param a_string: the string to hash
    :return: the hash value
    A slightly better hash function which takes the ord of each character to the 3rd power and adds
    them up to get the hash code
    '''
    current = 0
    for char in a_string:
        current = current + ord(char) ** 3
    return current


def collisions(filename, length, hash_func=hash):
    '''
    :param filename: the file to run
    :param length: size of the list to hash into
    :param hash_func: the hash function to test
    :return: average number of words before a collision is hit using the specified hash function
    '''
    total = 0
    for i in range(RUNS):
        a_list = [None] * length
        with open(filename) as file:
            count = 0
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                hash_code = hash_func(line)
                index = hash_code % length
                if a_list[index] is None:
                    a_list[index] = line
                    count += 1
                else:
                    break
        total += count
    return int(total / RUNS)

def time_hash(hash_func, size):
    start = time.perf_counter()
    for _ in range(size):
        hash_func("Hash me please")
    end = time.perf_counter()
    print(f"Time to hash {size} items with {hash_func.__name__:<15}: {(end - start):.3f}")


def main():
    '''
    Run the various hash functions through the collision detection function to compare collision performance
    '''
    hash_functions = [worst_hash_ever, str_hash_1, str_hash_2, str_hash_3, hash]
    sizes = [10, 100, 500, 5000, 50000]
    for hash_func in hash_functions:
        print('Hash function: ', hash_func.__name__)
        for size in sizes:
            print('hashes before collision in size ' + str(size) + ':', collisions(DATA_FILE, size, hash_func))
        print()

    perf_size = 5000000
    for hash_func in hash_functions:
        time_hash(hash_func, perf_size)


if __name__ == '__main__':
    main()
