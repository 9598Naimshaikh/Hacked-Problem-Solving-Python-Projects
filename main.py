## Some PYTHON Hacked Code.....

# *args  = allows you to pass multiple non-key arguments
# **kwargs = allow you to pass multiple keyword-arguments
#           * unpacking operator
#           1. Positional 2. Default 3. Keyword 4. ARBITRARY

"""
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(add(2, 3, 4, 2, 9))


def display_name(*names):
    for name in names:
        print(name, end=' ')


display_name('Coder', 'Naim', 'Shaikh')
"""

"""
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(F'{key}: {value}')


print_address(location='LIG Colony',
              city='Kurla West',
              pincode=400070,
              mob=9598489890)
"""

# def shaping_libel(*args, **kwargs):
#     for arg in args:
#         print(arg, end=' ')
#     print()
#
#     print(f'{kwargs.get("location")}')
#     print(f'{kwargs.get("city")} {kwargs.get("pincode")} {kwargs.get("main_city")}')
#
#
# shaping_libel('Coder', 'Naim', 'Shaikh',
#               location='LIG Colony',
#               city='Kurla West',
#               pincode=400070,
#               main_city='Mumbai')


# Map, Filter, Reduce.Function....
# def square(n):
#     return n * n
#
# def cube(n):
#     return n * n * n
#
# num = [3, 2, 5, 6]
# sq_num = []
# for n in num:
#     # sq_num.append(square(n))
#     sq_num.append(cube(n))
#
# print(sq_num)
"""
num = [2, 3, 5, 6, 6]
square_num = map(lambda x: x * x, num)
print(list(square_num))

cube_num = map(lambda x: x * x * x, num)
print(list(cube_num))
"""

# filter....
# l = [2, 4, 6, 7, 3, 9, 12, 10]
#
# # new_l = []
# # for n in l:
# #     if n > 4:
# #         new_l.append(n)
# #
# # print(new_l)
#
# greater_num = filter(lambda x: x > 4, l)
# print(list(greater_num))


# Reduce function.
# from functools import reduce
#
# list1 = [2, 3, 5, 1, 7]
# # total = sum(list1)
# # print(total)
#
# total = reduce(lambda x, y: x + y, list1)
# print(total)


## Factorial Number: ....
# def factorial_num(num):
#     return 1 if(num == 0 or num == 1) else num * factorial_num(num-1)
#
#
# print(factorial_num(n := int(input('Enter a number: '))))

"""
def factorial_num(num):
    if num < 0:
        return 'Invalid input.! Please enter a positive number.'
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial_num(num-1)


if __name__ == "__main__":
    num = int(input('Enter a number: '))
    print(factorial_num(num))

"""

# def factorial(num):
#     if num < 0:
#         return "Invalid input.! Please enter a positive number."
#     elif num == 0 or num == 1:
#         return 1
#     else:
#         fact = 1
#         while num > 1:
#             fact *= num
#             num -= 1
#         return fact
#
#
# if __name__ == "__main__":
#     n = int(input('Enter a num: '))
#     print(factorial(n))


# Question: Implement a Stack Using a Linked List
'''
class Stack:

    def __init__(self):
        self._items = []

    def push(self, data):
        """Adds an element with the given data to the top of the stack."""
        self._items.append(data)

    def pop(self):
        """Removes and returns the top element from the stack. If the stack is empty, return None."""
        return self._items.pop()

    def is_empty(self):
        """Returns True if the stack is empty, otherwise returns False."""
        if not self._items:
            return True
        else:
            return False

    @property
    def items(self):
        return self._items


stack1 = Stack()

stack1.push(34)
stack1.push("Naim")
stack1.push(89.80)

print(stack1.pop())
print(stack1.items)

print(stack1.is_empty())
'''

# simple Calculator Program
'''
def add():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"Result: {num1} + {num2} = {num1 + num2}")


def sub():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"Result: {num1} - {num2} = {num1 - num2}")


def multiply():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"Result: {num1} * {num2} = {num1 * num2}")


def divide():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"Result: {num1} / {num2} = {num1 / num2}")


if __name__ == "__main__":
    print("Simple Calculator")

    while True:
        try:
            print("------------------")
            print("\n1. Addition \
            \n2. Subtraction \
            \n3. Multiplication \
            \n4. Division \
            \n5. Quit\n")

            user_choice = int(input('Enter your choice $: '))

            if user_choice == 1:
                add()
            elif user_choice == 2:
                sub()
            elif user_choice == 3:
                multiply()
            elif user_choice == 4:
                divide()
            elif user_choice == 5:
                print("GoodBye!")
                break
        except Exception as e:
            print(e)
'''

# import re
#
#
# def strong_password_checker(password):
#     if len(password) < 8:
#         return "Weak password! Password should be at least 8 characters."
#
#     if not re.search(r"[A-Z]", password):
#         return "Weak password! Password should be contain at least one capital letter"
#
#     if not re.search(r"[a-z]", password):
#         return "Weak password! Password should be contain at least one lowercase letter."
#
#     if not re.search(r"[0-9]", password):
#         return 'Weak password! Password should be contain at least one digit (0-9).'
#
#     if not re.search(r"[!@#$%^*()_+~`;.,<>/?{}|]", password):
#         return "Weak password! Password should be contain at least one special character."
#
#     return "Strong Password"
#
#
# if __name__ == "__main__":
#     password = input('Enter Password $: ')
#     print(strong_password_checker(password))


"""
import string
import random
import re


def password_strength_checker(password):
    if len(password) < 8:
        return "Weak password! Password should be minimum 8 characters long."

    if not re.search(r'[A-Z]', password):
        return 'Weak password! Password should be contain at least one uppercase letter.'

    if not re.search(r'[a-z]', password):
        return 'Weak password! Password should be contain at least one lowercase letter.'

    if not re.search(r'[0-9]', password):
        return 'Weak password! Password should be contain at least one digit (0-9).'

    if not re.search(r'[!"#$%&()*+,-./:;<=>?@[\]^_`{|}~]', password):
        return 'Weak password! Password should be contain at least one special character.'

    return f'Strong Password: {password}'


def random_pass_gen():
    str_upper = string.ascii_uppercase
    str_lower = string.ascii_lowercase
    digit = string.digits
    special_character = string.punctuation

    password = []

    password.extend(list(str_lower))
    password.extend(list(str_upper))
    password.extend(list(digit))
    password.extend(list(special_character))

    password_length = int(input("Enter password length: "))

    random.shuffle(password)
    password = "".join(password[0:password_length])
    # print(password)
    print(password_strength_checker(password))


if __name__ == "__main__":
    random_pass_gen()
"""


# Todo: Question: Write a Python function called reverse_string that takes a string as input and returns the reversed
#  version of that string.

# def reverse_string(text):
#     reverse_word = text[::-1]
#     return reverse_word
#
#
# if __name__ == "__main__":
#     user_text = input("Enter a word which do you want to reverse: ")
#     print(reverse_string(user_text))


# Todo: Prime number checker
# def prime_num(num):
#     if num <= 1:
#         return "Not Prime number"
#     for i in range(2, int(num ** 0.5) + 1):
#         if num%i == 0:
#             return "Not Prime number"
#     return "Prime Number"
#
#
# if __name__ == "__main__":
#     number = int(input('enter numb: '))
#     print(prime_num(number))


# Todo: Problem: Find the Sum of Digits
#
# Write a Python function that takes an integer as input and calculates the sum of its digits.
#
# For example:
#
# Input: 12345
# Output: 15 (1 + 2 + 3 + 4 + 5)
"""
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


# Test the function
num = int(input("Enter an integer: "))
result = sum_of_digits(num)
print(f"The sum of digits in {num} is {result}")
"""


# number = int(input("Enter numbers: "))
# num = str(abs(number))
# total = 0
# for n in num:
#     total += int(n)
# print(total)



# Todo: Random Password Genrator using python.
"""
import random
import string

password_len = int(input("Enter password length: "))

my_password = ""
for i in range(password_len):
    my_password += random.choice(string.printable)


print(f"PASSWORD: {my_password}")
"""
