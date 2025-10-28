int_set = set()
for i in range(0,30,3):
    int_set.add(i)
for ele in int_set:
    print(ele, end = ' ')
print()

string_set = set("Here is the string we are adding to a set")
print(string_set)
sorted_set = sorted(string_set)
for ele in sorted_set:
    print(ele, end = ' ')
print()

a_dict = {}
for i in range(10):
    a_dict[i] = 30-i
print(a_dict)
print(a_dict.keys())
print(a_dict.values())
print(type(a_dict.items()))
s = sorted(a_dict.items(), key = lambda x:x[1])
print(s)