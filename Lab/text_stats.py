import matplotlib.pyplot as plt
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


# print(readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\very_short.txt"))
def totalOccurrences(word, data):
    total =0
    keys = data.keys()
    if word in keys:
        for items in data[word].values():
            total+=items
    return total

def letter_dict(data):
    letters = {l: 0 for l in "abcdefghijklmnopqrstuvwxyz" }
    words =data.keys()
    for i in words:
        for j in i:
            numbers = sum(x for x in data[i].values())
            letters[j]+=numbers

    return letters

def letterFreq(data):
    letter_dict_values = letter_dict(data)
    x = sorted(letter_dict_values, key = letter_dict_values.get, reverse = True)
    naked = ""
    for y in x:
        naked+=y
    return naked

# letterFreq(readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\a.txt"))

def letterFreqPlot(data):
    letter_dict_values = letter_dict(data)  
    plt.bar(list(letter_dict_values.keys()), list(letter_dict_values.values()), color='skyblue')
    plt.show()
# letterFreqPlot(readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\a.txt"))


def printedWords(data):
    a={}
    for i in data:
        for j in data[i]:
            if j not in a:
                a[j] = 0
            a[j]+=data[i][j]
    naked = []
    for y in a:
        naked.append((y,a[y]))
    return sorted(naked)


def wordsForYear(year, data):
    for i in data:
        if year in i:
            return i[1]

def printedWordsPlot(data):
    printed_values = data  
    years = [year for year , _ in printed_values]
    totals = [count for _, count in printed_values]
    plt.plot(years, totals, color='skyblue')
    plt.show()


def trending(data, starts, end):
    trend = []
    trend_value = 0
    for i in data:
        if starts in data[i] and end in data[i] and data[i][starts]> 1000 and data[i][end]>1000:
            trend_value=data[i][end]/ data[i][starts]
            trend.append((i, trend_value))
    trend.sort(key=lambda x: x[1], reverse=True)
    return trend
            
            
def trendingTopBottom(data, start, end):
    trends = trending(data, start, end)
    top3 = trends[:3]
    bottom3 = trends[-3:]
    print("Top: 3")
    for w, _ in top3:
        print(w)

    print("Bottom: 3")
    for w, _ in bottom3:
        print(w)




# trending(readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\very_short.txt"), 2005, 2008)
trendingTopBottom(readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\a.txt"), 1966, 1975 )

# printedWordsPlot(printedWords(readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\a.txt")))
# printedWords(readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\very_short.txt"))
# wordsForYear(1900,printedWords(readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\z.txt")))
def main():
    pass
    # a=input("enter a word file: ")
    # b=input("enter a word: ")
    # print(totalOccurances(b,readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\very_short.txt")))
main()

# data[airport][year] = 