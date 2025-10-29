"""
CS1 Lab 7, 2251
Instructor: Tony Audi
Author: Abdulaziz
"""
import matplotlib.pyplot as plt

def readWordFile(filename):
    """Reads a data file and stores the information in a dictionary inside the dictionary {word: {year: count}}"""
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

def totalOccurrences(word, data):
    """Returns the total number of times a given word appears for all years"""
    total =0
    keys = data.keys()
    if word in keys:
        for items in data[word].values():
            total+=items
    return total

def letter_dict(data):
    """Counts how many times each letter appears in all words, times by their total for all years."""
    letters = {l: 0 for l in "abcdefghijklmnopqrstuvwxyz" }
    words =data.keys()
    for i in words:
        for j in i:
            numbers = sum(x for x in data[i].values())
            letters[j]+=numbers

    return letters

def letterFreq(data):
    """Return letters sorted by frequency, from most to least common"""
    letter_dict_values = letter_dict(data)
    x = sorted(letter_dict_values, key = letter_dict_values.get, reverse = True)
    freq = ""
    for y in x:
        freq+=y
    return freq


def letterFreqPlot(data):
    """Creates a bar chart showing how often each letter appears with matplotlib"""
    letter_dict_values = letter_dict(data)  
    plt.bar(list(letter_dict_values.keys()), list(letter_dict_values.values()), color='skyblue')
    plt.show()


def printedWords(data):
    """Returns a sorted list of year, total count pairs showing total printed words per year"""
    a={}
    for i in data:
        for j in data[i]:
            if j not in a:
                a[j] = 0
            a[j]+=data[i][j]
    words = []
    for y in a:
        words.append((y,a[y]))
    return sorted(words)


def wordsForYear(year, data):
    """Finds and returns the total count of printed words for a given year"""
    for i in data:
        if year in i:
            return i[1]

def printedWordsPlot(data):
    """Plots how total printed words change over the years. """
    printed_values = data  
    years = [year for year , _ in printed_values]
    totals = [count for _, count in printed_values]
    plt.plot(years, totals, color='skyblue')
    plt.show()


def trending(data, starts, end):
    """Calculates how much each words usage changed between two years and returns a sorted list of word and value """
    trend = []
    trend_value = 0
    for i in data:
        if starts in data[i] and end in data[i] and data[i][starts]> 1000 and data[i][end]>1000:
            trend_value=data[i][end]/ data[i][starts]
            trend.append((i, trend_value))
    trend.sort(key=lambda x: x[1], reverse=True)
    return trend


                   
def trendingTopBottom(data, start, end):
    """Prints the top three and bottom three words based on their trend ratios."""
    trends = trending(data, start, end)
    top3 = trends[:3]
    bottom3 = trends[-3:]
    print("Top: 3")
    for w in top3:
        print(w[0])

    print("Bottom: 3")
    for  w in bottom3:
        print(w[0])

def main():
    """Runs a if else program for testing that works with all the functions above. its easier that way to test it. """
    filename = input("Enter word file: ").strip()
    data = readWordFile(filename)

    print("1. Total occurrences of a word")
    print("2. Letter frequency (sorted)")
    print("3. Letter frequency plot")
    print("4. Printed words by year")
    print("5. Printed words plot")
    print("6. Trending, word ratios between two years. ")
    print("7. Top/Bottom trending words")
    choice = input("Enter choice (1–7): ").strip()

    if choice == "1":
        word = input("Enter word: ").strip()
        total = totalOccurrences(word, data)
        print("Total occurrences of", word, total)

    elif choice == "2":
        print("Letter frequency order:")
        print(letterFreq(data))

    elif choice == "3":
        print("Generating letter frequency plot...")
        letterFreqPlot(data)

    elif choice == "4":
        result = printedWords(data)
        print("Printed words per year:")
        for year, count in result:
            print(year, count)

    elif choice == "5":
        print("Generating printed words plot...")
        printedWordsPlot(printedWords(data))

    elif choice == "6":
        start = int(input("Enter start year: ").strip())
        end = int(input("Enter end year: ").strip())
        result = trending(data, start, end)
        if not result:
            print("No valid words found for those years.")
        else:
            print("Trending results:")
            for word, value in result:
                print(word, value)

    elif choice == "7":
        start = int(input("Enter start year: ").strip())
        end = int(input("Enter end year: ").strip())
        trendingTopBottom(data, start, end)

    else:
        print("Invalid choice. Run the program again and pick a number 1–7.")

    # print(totalOccurances(b,readWordFile(r"C:/Users\acapt\OneDrive\Desktop\CSCI 141\Lab\data\very_short.txt")))
if __name__ == "__main__":
    main()