def is_palindrome(word):
    """
    A boolean function that iteratively tests whether a word is a palindrome
    or not.
    :param word: the word
    :return: whether it is a palindrome or not
    """
    return False

def is_palindrome_rec(word):
    """
    A boolean function that recursively tests whether a word is a palindrome
    or not.
    :param word: the word
    :return: whether it is a palindrome or not
    """
    return False

def main():
    """
    Prompt the user to enter a word and detect whether it is a palindrome
    or not.
    :return: None
    """
    word = input('Enter a word: ')
    print('Is ' + word + ' a palindrome?', is_palindrome(word))
    print('Is ' + word + ' a palindrome?', is_palindrome_rec(word))

if __name__ == '__main__':
    main()