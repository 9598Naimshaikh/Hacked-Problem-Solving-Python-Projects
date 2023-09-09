# 3. Prime Number Checker

# Write a Python function that checks whether a given integer is a prime number or not. A prime number is a positive
# integer greater than 1 that has no positive integer divisors other than 1 and itself. Write a function named
# is_prime that takes an integer as input and returns True if it's a prime number and False otherwise.

def is_prime(num):
    """check if number is prime
    num: The number to check
    Return: True if the number is prime, otherwise False"""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(is_prime(2))
    print(is_prime(5))
    print(is_prime(49))
    # print(is_prime.__doc__)
