"""
CS1 Homework 6, 2251
Author: RIT CS faculty
Author: YOUR NAME HERE
"""

# QUESTION 1

def words_containing(words,c):
    return [i for i in words if c in i]

print(words_containing(['hello','world'],'r'))
# QUESTION 2

def square_tups(nums):
    pass

# QUESTION 3


def swap( lst, i, j ):
    """
    swap: List NatNum NatNum -> None
    swap the contents of list at pos i and j.
    Parameters:
        lst - the list of data
        i   - index of one datum
        j   - index of the other datum
    """
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def insert( lst, mark ):
    """
    insert: List(Orderable) NatNum -> None
    Move value at index mark+1 so that it is in its proper place.
    The mark is index of the last value in the sorted part.
    Parameters:
        lst - the list of data
        mark - represents cutting the list between
               index mark and index mark+1
    pre-conditions: lst[0:mark+1] is sorted.
    post-conditions: lst[0:mark+2] is sorted.
    """
    index = mark
    while index > -1 and lst[index] > lst[index+1]:
        swap( lst, index, index+1 )
        index = index - 1

def insertion_sort( lst ):
    """
    insertion_sort : List(Orderable) -> None
    Perform an in-place insertion sort on a list of orderable data.
    Parameters:
        lst - the list of data to sort
    post-conditions:
        The data list is in sorted order.
    """
    for mark in range( len( lst ) - 1 ):
        insert( lst, mark )

