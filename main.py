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





