"""
CS141 Week 9: Hashing

An implementation of a hash table that uses open addressing to resolve
collisions.

author: RIT CS
"""

from typing import Any, Hashable, Callable, Optional

def create_hash_table(capacity: int = 10) -> list:
    """
    Create a new empty hash table and return it.
    :param capacity: the capacity of the table
    :return: the new empty hash table
    """
    if capacity < 2:
        capacity = 2
    table = list()
    for _ in range(capacity):
        table.append((None, None))  # Use a tuple to store the key value pairs
    return table

def hash_table_to_str(hash_table: list) -> str:
    """
    Return a string representation of the hash table.
    :param hash_table: the hash table
    :return: a "stringified" hash table
    """
    result = ''
    for i in range(len(hash_table)):
        e = hash_table[i]
        result += str(i) + ': ' + str(e)  + '\n'
    return result

def keys(hash_table: list) -> list:
    """
    Return the keys in as hash table.
    :param hash_table: the hash table
    :return: a list of keys
    """
    result = list()
    for entry in hash_table:
        if entry[0] is not None:
            result.append(entry[0])
    return result

def values(hash_table: list) -> list:
    """
    Return the values in as hash table.
    :param hash_table: the hash table
    :return: a list of values
    """
    result = list()
    for entry in hash_table:
        if entry[1] is not None:
            result.append(entry[1])
    return result

def has(hash_table: list, key: Hashable, hash_func:Callable = hash) -> bool:
    """
    Check if a key exists in a hash table
    :param hash_table: the hash table
    :param key: they key to search for
    :param hash_func: the hash function to use.  Defaults to python hash
    :return: whether the key is in the table or not
    """
    index = hash_func(key) % len(hash_table)
    start_index = index
    while hash_table[index] is not None and hash_table[index][0] != key:
        index = (index + 1) % len(hash_table)
        if index == start_index:
            return False  # make sure not to go in circles
    return hash_table[index][0] != None

def put(hash_table: list, key: Hashable, value: Any, hash_func:Callable = hash) -> Any:
    """
    Put a key/value pair into the table.  If the key doesn't exist
    in the table, we add a new entry to a new location in the table.
    Otherwise we update the value of the existing entry.
    :param hash_table: the hash table
    :param key: the key
    :param value: the value
    :param hash_func: the hash function to use.  Defaults to python hash
    :return: if the key already exists, its old value, otherwise None
    """
    index = hash_func(key) % len(hash_table)
    start_index = index
    while hash_table[index][0] is not None and hash_table[index][0] != key:
        index = (index + 1) % len(hash_table)
        if index == start_index:
            _resize_rehash(hash_table, hash_func)  # resize and rehash if full
    if hash_table[index][0] is None:  # new entry, return None
        hash_table[index] = (key, value)
        return None
    else:                 # update existing entry, return old value
        old_value = hash_table[index][1]
        hash_table[index] = (key,value)
        return old_value

def get(hash_table: list, key: Hashable, hash_func:Callable = hash) -> Any:
    """
    Get the value associated with a key in the table
    :param hash_table: the hash table
    :param key: the key
    :param hash_func: the hash function to use.  Defaults to python hash
    :return: the value or None if the key doesn't exist
    """
    index = hash_func(key) % len(hash_table)
    start_index = index
    while hash_table[index] is not None and hash_table[index][0] != key:
        index = (index + 1) % len(hash_table)
        if index == start_index:
            return None
    if hash_table[index] is None:
        return None
    else:
        return hash_table[index][1]
    
def _resize_rehash(hash_table: list, hash_func:Callable = hash)->None:
    """
    Helper function to deal with a full table.
    Double the size of the table and rehash into the new table
    :param hash_table: the hash table
    :param hash_func: the hash function to use.  Defaults to python hash
    :return: None
    """
    print("Resizing ...")
    hash_table_copy = hash_table.copy()
    current_len = len(hash_table)
    for i in range(current_len):
        hash_table[i] = (None, None)
    for i in range(current_len):
        hash_table.append((None, None))
    for entry in hash_table_copy:
        key = entry[0]
        value = entry[1]
        put(hash_table, key, value, hash_func)
    print("Done!")


def main() -> None:
    """Show how to use the HashTable class."""
    h_table = create_hash_table()
    print(h_table)
    print(hash_table_to_str(h_table))
    print(put( h_table, "one", 1.0 ))
    print(put( h_table, "two", 2.0 ))
    print(put( h_table, "three", 3.0 ))
    print(put( h_table, "threefive", 3.5 ))
    print(put( h_table, "three", 3 ))
    print(keys(h_table))
    print(values(h_table))
    print(has(h_table, "one"))
    print(has(h_table, "four"))
    print(get(h_table, "one"))
    print(get(h_table, "four"))
    print(hash_table_to_str(h_table))

    for i in range(20):
        put(h_table, str(i), i)
    print(hash_table_to_str(h_table))
    print(len(keys(h_table)))
    print(sorted(keys(h_table)))

if __name__ == "__main__":
    main()
