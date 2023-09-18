# Question 18: Password Strength Checker

# Create a Python program that checks the strength of a password based on the following criteria:

# 1. The password must be at least 8 characters long.
# 2. The password must contain at least one uppercase letter.
# 3. The password must contain at least one lowercase letter.
# 4. The password must contain at least one digit (0-9).
# 5. The password must contain at least one special character (e.g., !, @, #, $, etc.).

# Your program should take a password as input and determine if it meets the above criteria. If the password meets
# all the criteria, it should be considered "strong." Otherwise, it should be considered "weak."

# Here's a sample interaction with the program:

"""
Password Strength Checker
-------------------------

Enter your password: MyP@ssw0rd
Strong password!

Enter your password: weak123
Weak password! Please follow the password criteria.
"""

# You can use regular expressions (re module in Python) to check for uppercase letters, lowercase letters, digits,
# and special characters.


import re


def password_strength_checker(password):

    # Check if the password is at least 8 characters long.
    if len(password) < 8:
        return "Weak password! Password should be at least 8 characters long"

    # Check if the password contain at least one uppercase letter.
    if not re.search(r'[A-Z]', password):
        return "Weak password! Password should be contain at least one uppercase letter."

    # Check if the password contain at least one lowercase letter.
    if not re.search(r'[a-z]', password):
        return "Weak password! Password should be contain at least one lowercase letter."

    # Check if the password contain at least one digit (0-9)
    if not re.search(r'[0-9]', password):
        return "Weak password! Password should be contain at least one digit."

    # Check if the password contain at least one special character.
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]", password):
        return "Weak password! Password should be contain at least one special character."

    return "Strong Password"


if __name__ == "__main__":
    print('Password Strength Checker')
    print("--------------------------")

    password = input("Enter a Password $: ")
    print(password_strength_checker(password))







