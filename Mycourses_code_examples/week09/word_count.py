"""
CS141 Week 9: Hashing

A word counting program that uses our open addressing hash table.

author: RIT CS Faculty
"""
import os
import hashtable   # create_hash_table, keys, values, get, put, has
current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/data/white_lightning.txt"
TABLE_CAPACITY = 100
# DATA_FILE = current_file_path + "/data/alice.txt"
# TABLE_CAPACITY = 1000

def read_words(filename: str) -> list:
    """
    Read the words from a file into a dictionary that counts the number of
    occurrences of each word.
    :param filename: the file to read
    :return: a dictionary whose keys are words and values are counts
    """
    words = hashtable.create_hash_table(TABLE_CAPACITY)
    with open(filename) as f:
        for line in f:
            for word in line.split():
                word = word.strip(",.\"\';:-!?").lower()
                if not hashtable.has(words, word):
                    hashtable.put(words, word, 1)
                else:
                    hashtable.put(words, word, hashtable.get(words, word)+1)
    return words

def main() -> None:
    """
    Count the words in a file and display some statistics.
    """
    words = read_words(DATA_FILE)
    print(hashtable.hash_table_to_str(words))
    print("Total words:", sum(hashtable.values(words)))
    print("Unique words:", len(hashtable.keys(words)))
    most = list(hashtable.values(words))
    most.sort()
    for word in hashtable.keys(words):
        if hashtable.get(words, word) == most[-1]:
            print('Most used word,', '"' + word + '"' + ' occurred',
                    hashtable.get(words, word), 'times.')

if __name__ == '__main__':
    main()