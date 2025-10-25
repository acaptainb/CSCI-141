def readWordFile(filename):
    main_dict=dict()
    with open(filename) as f:
        for line in f:
            w=line.strip().split(",")
            if len(w)==1:
                q=w[0]
                main_dict[w[0]]=dict()
            else:
                main_dict[q][int(w[0])] = int(w[1])
    return main_dict
print(readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\very_short.txt"))
def totalOccurances(word, data):
    total =0
    keys = data.keys()
    if word in keys:
        for items in data[word].values():
            total+=items
    return total

def letterFreq(data):
    a = ""
    words =data.keys()
    keys = data.values()
    for i in words:
        times = keys
        for j in i:
            print(j )
letterFreq(readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\very_short.txt"))


def main():
    pass
    # a=input("enter a word file: ")
    # b=input("enter a word: ")
    # print(totalOccurances(b,readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\very_short.txt")))
main()