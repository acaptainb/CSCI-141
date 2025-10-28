a_string = "This is a string"
# a_range = range(1,20,2)

target_sequence = a_string

# recursive sequence printer
print("Recursion")
def print_seq_recursive(sequence):
    if len(sequence) == 0:
        print()
    else:
        print(sequence[0], end = "|")
        print_seq_recursive(sequence[1:])
    return None

print_seq_recursive(target_sequence)

# iterative sequence printer using while
print("While Loop")
index = 0
while index < len(target_sequence):
    print(target_sequence[index], end="|")
    index += 1
print()

# iterative sequence printer using for
print("For Loop")
for element in target_sequence:
    print(element, end="|")
print()

with open("alice.txt") as my_file:
    for line in my_file:
        stripped = line.strip()
        print(len(stripped), stripped[:25:])
    # my_file.close()