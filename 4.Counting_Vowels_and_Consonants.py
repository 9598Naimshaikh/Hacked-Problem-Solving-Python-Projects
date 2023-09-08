# 4. Counting Vowels and Consonants

# Write a Python function that counts the number of vowels and consonants in a given string. Vowels are the letters
# 'a', 'e', 'i', 'o', and 'u' (case-insensitive), and consonants are all other alphabetic characters. Write a
# function named count_vowels_and_consonants that takes a string as input and returns a tuple containing the count of
# vowels and consonants, in that order.

def count_vowels_and_consonants(text):
    # text = text.lower().split()
    # new_text = ''.join(text)
    # print(new_text)
    text = text.lower()
    vowels = 0
    consonants = 0
    for char in text:
        if char in 'aeiou':
            vowels += 1
        elif char.isalpha():
            consonants += 1
    return vowels, consonants


if __name__ == '__main__':
    user_str = 'Hello World'
    print(count_vowels_and_consonants(user_str))
    print(count_vowels_and_consonants("Programming is fun"))
    print(count_vowels_and_consonants('Rhythm'))
