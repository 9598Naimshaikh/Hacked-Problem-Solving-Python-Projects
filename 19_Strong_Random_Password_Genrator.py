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
