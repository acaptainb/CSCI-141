def does_file_contain_word(filename:str, word:str)->bool:
    result = False
    with open(filename) as file:
        for line in file:
            stripped = line.strip()
            if stripped == word:
                result = True
                break
    return result

def main():
    done = False
    filename = input('Enter a file to search:')
    while not done:
        word = input('Enter a word to look for')
        if does_file_contain_word(filename, word):
            print(filename, ' contains ', word)
        else:
            print(filename, ' does NOT contain ', word)
        answer = input('Do you want to try again (y/n):')
        if answer == 'n' or answer == 'N' or answer == 'No':
            done = True
    print('Thanks for trying')

if __name__ == '__main__':
    main()