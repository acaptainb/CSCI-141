import re
import os

current_file_path = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = current_file_path + "/data/war-n-peace.txt"

word_counts = dict()
total = 0
with open(DATA_FILE,'r',encoding='utf8') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            word = re.sub("[^A-Z]", "", word,0,re.IGNORECASE) # get rid of all non letters
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1
            total += 1
# for key in word_counts:
#     print(key, word_counts[key])
print('Total words = ', total)

sorted_word_counts_by_count = sorted(word_counts.items(), key = lambda x:x[1], reverse=True)
print(type(sorted_word_counts_by_count))
top_20_word_counts = sorted_word_counts_by_count[:20]
for item in top_20_word_counts:
    print(item, type(item))
print(len(word_counts))
