def file_type(fn):
    if fn[-4:]=='.txt':
        print('Text')
    elif fn[-5:-1]=='.mud':
        print('Mud')
    else:
        print('neither')

# print(file_type('muudle.txt'))

def other_fileName(fn):
    if fn[-4:]=='.txt':
        return fn[:-4] + '.mud4'
    elif fn[-5:-1]=='.mud':
        return fn[:-5] + '.2.txt'
# print(other_fileName('8974.txt'))


def shift(s:str,n:int):
    total=""
    for i in s:
        total+=chr(ord(i)+n)
    return total



def muddle(text, keyword, n):
    result = ""
    for char in text:
        shifted = ord(char) + n
        if char in keyword:
            shifted += 110
        result += chr(shifted)
    return result


def clarify(text, n):
    result = ""
    for char in text:
        code = ord(char)
        if code >135:
            code-=110+n
        else:
            code-=n
        result += chr(code)
    return result


# code = muddle('Hello there, universe!', 'abcdefg', 9)
print(muddle('Hello there, universe!', '!', 3))
# print(clarify(code, 9))
# print(shift("abdulaziz",109))