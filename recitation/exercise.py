"""
CSCI-141 Computer Science 1 Recitation Exercise
09- Dictionaries and Structures

Using a list of baby names from the file ny.txt, we would like to find
how many unique names there are and what the total number of occurrences
of a given name is.

The format of the file is one record per line:

state,gender,year,name,count

For example:

NY,M,2013,Teddy,5

This is the starter code for the students.  Use the TODO's to guide
you in completing this assignment.
"""

from dataclasses import dataclass

def read_file(filename):
    """
    Takes a filename as input and reads each line into a Record structure object
    and adds it to a list.
    :param filename: the file with the names
    :return: a list of name/count tuples
    """
    names = list()
    with open(filename) as file:
        for line in file:
            # extract the fields from the next line
            fields = line.strip().split(',')
            name = fields[3]
            count = int(fields[4])
            names.append((name, count))
            # TODO: Step 1 - create and add a new name/count tuple to the names list

    return names

def build_dictionary(names):
    """
    Create and build a dictionary of names to total occurrences from a list of
    name/count tuples.
    :param names: a list of name/count tuples
    :return: dictionary of names to counts
    """
    counts = dict()
    for name, count in names:
        if name in counts:
            counts[name] += count
        else:
            counts[name] = count
    # TODO: Step 2 - build and return the dictionary

    return counts

def main():
    """
    The main program.
    """

    # first read the file into a list of Record's
    names = read_file("scratch.txt")

    # next, build a dictionary of names to total counts
    counts = build_dictionary(names)
    print('There are', len(counts), 'unique names!')

    # prompt for a name to search for and retrieve it from the dictionary
    find_name = input("Enter a name to search for: ")
    find_name = find_name.capitalize()
    if find_name in counts:
        print(find_name, 'appeared', counts[find_name], 'times')
    else:
        print(find_name, 'not found!')

    # display the names and their counts alphabetically
    response = input('Display all names alphabetically? (y/n): ')
    if response.lower() == 'y':
        sorted_names = sorted(counts.keys())
        # TODO: Step 3 - print each sorted name and overall count in the format: "name -> count"
        print(sorted_names)

if __name__ == '__main__':
    main()
