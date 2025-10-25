"""
CS1 Homework 8, 2251
Author: Abdulaziz Abbasov
"""

# b={"Blinding Lights": 3.2, "Save Your Tears": 4.0, "Starboy": 3.5}
# for i in b:
#     print(b[i])
def listen(num_plays, title):
    ''' returns num_plays + 1 if that song has been played , or if its new , it adds to the dict'''
    if title in num_plays:
        num_plays[title] = num_plays[title] + 1
    else:
        num_plays[title] = 1
    return num_plays


def total_listen_time(lengths, num_plays):
    ''' calculates total listening time by lenghts or the song and number of plays'''
    total_time = 0
    for i in num_plays:
        total_time += lengths[i] * num_plays[i]
    return total_time



def coll_check(tab, k):
    ''' determines the number of collisions for rehashing'''
    index = hash(k)%len(tab)
    count = 0
    while tab[index] is not None:
        if tab[index][0] ==k:
            return count
        count += 1
        index =(index+1) % len(tab)
    return count



if __name__ == "__main__":
    pass
