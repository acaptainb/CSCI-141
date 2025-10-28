from typing import Callable, Any
from hash_functions import *
import os
current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/data/war-n-peace.txt"

SIZES = [10000]
HASH_FUNCTIONS = [worst_hash_ever, str_hash_1, str_hash_2, str_hash_3, hash]

def make_chaining_set(capacity:int):
    set_table = []
    for _ in range(capacity):
        set_table.append([])
    return set_table


def add(myset:list, element:any, hash_func:Callable):
    capacity = len(myset)
    index = hash_func(element) % capacity
    row = myset[index]
    for entry in row:
        if entry == element:
            return
    myset[index].append(element)


def contains(myset:list, element:any, hash_func:Callable):
    capacity = len(myset)
    index = hash_func(element)%capacity
    row = myset[index]
    for elt in row:
        if elt == element:
            return True
    return False


def main():
    for hash_func in HASH_FUNCTIONS:
        print('Hash function: ', hash_func.__name__)
        for size in SIZES:
            myset = make_chaining_set(size)
            with open(DATA_FILE,'r',encoding='utf8') as file:
                for line in file:
                    words = line.strip().split()
                    for word in words:
                        add(myset, word, hash_func)
            max = 0
            empty = 0
            for row in myset:
                row_len = len(row)
                # print(row_len, row)
                if row_len > max:
                    max = row_len
                if row_len == 0:
                    empty += 1
            print('{:10s}{:6d}\t|\t'.format('Set Size = ', size), end = '')
            print('{:15s}{:6d}\t|\t'.format('Maximum chain length = ', max), end = '')
            print('{:15s}{:6d}\t|\t'.format('Number of empty slots = ', empty))
        print()


if __name__ == '__main__':
    main()