# 5. Check for Palindrome
#
# Write a Python function that checks if a given string is a palindrome. A palindrome is a word, phrase, number,
# or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation,
# and capitalization).

# Write a function named is_palindrome that takes a string as input and returns True if it's a palindrome and False
# otherwise.

import string


def is_palindrome(words):
    """
    1: Converting the input to lowercase to ensure case insensitivity.
    2: Removing punctuation and spaces to focus on the actual characters.
    3: Reversing the cleaned string.
    4: Comparing the original and reversed strings to determine if it's a palindrome.
    :param words:
    :return:
    """
    word_l = words.lower().split()
    word_s = ''.join(word_l)

    remove_punc_word = word_s.translate(str.maketrans('', '', string.punctuation))
    # print(remove_punc_word)
    reverse_word = remove_punc_word[::-1]
    # print(reverse_word)
    if remove_punc_word == reverse_word:
        # return True
        return 'Yes Palindrome.!'
    else:
        # return False
        return 'Not Palindrome.!'


if __name__ == "__main__":
    word = 'Hello World.!!>>>???'
    print(is_palindrome(word))
    print(is_palindrome("racecar"))
    print(is_palindrome("A man, a plan, a canal, Panama"))
    # print(is_palindrome.__doc__)
