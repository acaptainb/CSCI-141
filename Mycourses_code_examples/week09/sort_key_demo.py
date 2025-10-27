DATA_FILE = "sort_key_demo_data.txt"

def create_people_list(filename):
    people_list = []                            # create the list we are building
    with open(filename) as f:                   # open the data file
        next(f)                                 # get rid of the header line
        for line in f:                          # iterate through the file
            data = line.strip().split(",")      # grab a line of data and split it on commas into a list
            name = data[0]                      # get each piece of data for a person
            age = data[1]
            weight = data[2]
            person = (name, age, weight)        # build the person as a tuple
            people_list.append(person)          # add the new person to the list
    return people_list                          # return the complete list of people

def sort_key(item):
    return item[1]

def main():
    # create a randomly ordered list of number and print it
    nums = [3,5,1,6,9,8,2,7,4]
    print("Random ordered numbers:\t\t", nums)

    # sort the nums into a new list and print it
    sorted_nums = sorted(nums)
    print("Sorted numbers:\t\t\t\t",sorted_nums)

    # reverse sort the nums into a new list and print it
    reversed_sorted_nums = sorted(nums, reverse=True)
    print("Reverse Sorted numbers:\t\t",reversed_sorted_nums)

    print()
    # read the list of people and print it
    people = create_people_list(DATA_FILE)
    print("Unsorted people:\t\t\t", people)

    # sort the people by age using a sort key and print the updated list
    people.sort(key=sort_key)
    print("People sorted by age:\t\t", people)

    # sort the people by weight into a new list using a lambda and print it
    people_sorted_by_weight = sorted(people, key=lambda x: x[2])
    print("People sorted by weight:\t",people_sorted_by_weight)

if __name__ == '__main__':
    main()
