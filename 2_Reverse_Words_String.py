# 2. Reverse Words in a String

# Write a Python function that reverses the order of words in a given string. A word is defined as a sequence of
# non-space characters separated by a space. Write a function named reverse_words that takes a string as input and
# returns the string with the words reversed.

def reverse_word(word):
    word_list = word.split()
    word_list.reverse()
    revers_word = ' '.join(word_list)
    print(revers_word)


if __name__ == '__main__':
    reverse_word("Hello World")
    reverse_word('Naim Shaikh')
