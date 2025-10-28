"""
CSAPX Week 9: Hashing

An implementation of a hash table that uses open addressing to resolve
collisions. The difference from hashtable.py is that this version
uses an object-oriented design. HashTable is a full class with methods.

This version does not implement rehashing and when the size reaches
the capacity an exception will be thrown if a new entry is added.

author: RIT CS
"""

from dataclasses import dataclass
from typing import Any, Hashable, Callable, Optional
from car_class import *
import os

current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/car_data.csv"

# Use a dataclass to represent the key / value pair
@dataclass
class Entry:
    """
    A class used to hold key/value pairs.
    key: hashable key
    value: any value
    """
    key: Hashable
    value: Any


def entry_to_str( entry: Entry ) -> str:
    """
    Return a string representation of an entry.
    :param entry: the entry
    :return: a string containing the key and value
    """
    return '(' + str( entry.key ) + ', ' + str( entry.value ) + ')'

# Use a full class for the hashtable
class HashTable:
    """
    The HashTable data structure contains a collection of values
    where each value is located by a hashable key.
    No two values may have the same key, but more than one
    key may have the same value.
    table: is the list holding the hash table
    size: is the number of elements in occupying the hash table
    capacity: the max capacity of the table
    hash_func: the hash function for the key
    """
    table: list[Optional[Entry]]
    size: int
    capacity: int
    hash_func: Callable[[Hashable],int] # a function of (Hashable) -> int

    def __init__( hash_table: "Hashable",
                  hash_function: Callable[[Hashable],int],
                  capacity: int) -> None:
        """
        Create a new empty hash table and return it.
        :param hash_function: the immutable key's hash function
        :param capacity: the capacity of the table
        :return: the new empty hash table
        """
        if capacity < 2:
            capacity = 2
        hash_table.table = list()
        for i in range(capacity):
            hash_table.table.append(None)
        hash_table.size = 0
        hash_table.capacity = capacity
        hash_table.hash_func = hash_function

    def __str__(hash_table: "HashTable") -> str:
        """
        Return a string representation of the hash table.
        :param hash_table: the hash table
        :return: a "stringified" hash table
        """
        result = ''
        for i in range(hash_table.capacity):
            e = hash_table.table[i]
            if e is not None:
                result += str(i) + ': '
                result += entry_to_str(e) + '\n'
            else:
                result += str(i) + ': None' + '\n'
        return result

    def keys(hash_table: "HashTable") -> list[Hashable]:
        """
        Return the keys in as hash table.
        :param hash_table: the hash table
        :return: a list of keys
        """
        result = list()
        for entry in hash_table.table:
            if entry is not None:
                result.append(entry.key)
        return result

    def values(hash_table: "HashTable") -> list[Any]:
        """
        Return the values in as hash table.
        :param hash_table: the hash table
        :return: a list of values
        """
        result = list()
        for entry in hash_table.table:
            if entry is not None:
                result.append(entry.value)
        return result

    def has(hash_table: "HashTable", key: Hashable) -> bool:
        """
        Check if a key exists in a hash table
        :param hash_table: the hash table
        :param key: they key to search for
        :return: whether the key is in the table or not
        """
        index = hash_table.hash_func(key) % hash_table.capacity
        start_index = index
        while hash_table.table[index] is not None and \
              hash_table.table[index].key != key:
            index = (index + 1) % hash_table.capacity
            if index == start_index:
                return False  # make sure not to go in circles
        return hash_table.table[index] != None

    def put(hash_table: "HashTable", key: Hashable, value: Any) -> Any:
        """
        Put a key/value pair into the table.  If the key doesn't exist
        in the table, we add a new entry to a new location in the table.
        Otherwise we update the value of the existing entry.
        :param hash_table: the hash table
        :param key: the key
        :param value: the value
        :raise Exception if the hash table is full
        :return: if the key already exists, its old value, otherwise None
        """
        index = hash_table.hash_func( key) % hash_table.capacity
        start_index = index
        while hash_table.table[index] is not None and \
              hash_table.table[index].key != key:
            index = (index + 1) % hash_table.capacity
            if index == start_index:
                raise Exception("Hash table is full.")
                                   # make sure not to go in circles
        if hash_table.table[index] is None:  # new entry, return None
            hash_table.table[index] = Entry(key, value)
            hash_table.size += 1
            return None
        else:                        # update existing entry, return old value
            old_value = hash_table.table[index].value
            hash_table.table[index].value = value
            return old_value

    def get(hash_table: "HashTable", key: Hashable) -> Any:
        """
        Get the value associated with a key in the table
        :param hash_table: the hash table
        :param key: the key
        :raise Exception if the table does not contain the key
        :return: the value
        """
        index = hash_table.hash_func(key) % hash_table.capacity
        start_index = index
        while hash_table.table[index] is not None and \
              hash_table.table[index].key != key:
            index = (index + 1) % hash_table.capacity
            if index == start_index:
                raise Exception("Hash table does not contain key.")
                                       # make sure not to go in circles
        if hash_table.table[index] is None:
            raise Exception("Hash table does not contain key:", key)
        else:
            return hash_table.table[index].value

def main() -> None:
    """Show how to use the HashTable class."""
    h_table = HashTable( hash, 50 )
    with open(DATA_FILE) as file:
        next(file)
        for row in file:
            row = row.strip().split(",")
            new_car = Car(row[0],float(row[1]),float(row[3]))
            h_table.put(new_car.model, new_car)

    print( h_table )

if __name__ == "__main__":
    main()
