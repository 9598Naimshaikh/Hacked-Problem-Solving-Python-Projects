# Question 21: Count Words in a Text

# Write a Python program that counts the number of words in a given text. The program should do the following:

# 1. Prompt the user to enter a text string.
# 2. Tokenize the text into words (assume words are separated by spaces).
# 3. Count the number of words in the text.
# 4. Print the total count of words in the text.

# Your program should handle different cases, punctuation, and multiple spaces between words.
# text = "This is a sample sentence. How many words are in this text?"
# output: Total Words in the text: 11

import string


def count_words():
    """
    1.Prompt the user to enter a text string.
    2.Tokenize the text into words (assume words are separated by spaces).
    3.Count the number of words in the text.
    4.Print the total count of words in the text.
    5.don't count same word in multiple time only count one time.
    return = return the total word in user_input text.
    """
    user_input = input("Enter your text: ")

    remove_punc = user_input.translate(str.maketrans("", "", string.punctuation)).lower()

    tokenize_text = set(remove_punc.split())

    total_words = len(tokenize_text)
    print(F'Total word in the text: {total_words}')


if __name__ == "__main__":
    count_words()
    # print(count_words.__doc__)
