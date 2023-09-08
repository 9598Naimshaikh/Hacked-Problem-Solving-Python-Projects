# 7. Two Sum

# Write a Python function that finds two numbers in a given list of integers such that they add up to a specific
# target number. You may assume that each input would have exactly one solution, and you cannot use the same element
# twice.
# Write a function named two_sum that takes a list of integers nums and an integer target as input and returns a list
# of two integers that add up to the target.

import random


def two_sum(nums, target):
    while True:
        choice1 = random.choice(nums)
        choice2 = random.choice(nums)
        if choice1 + choice2 == target:
            num_l = choice1, choice2
            two_nums = list(num_l)
            return two_nums


if __name__ == '__main__':
    print(two_sum([2, 3, 5, 6], 8))  # Output: [6, 2]
    print(two_sum([2, 7, 11, 15], 9))  # Output: [7, 2]
    print(two_sum([3, 2, 4], 6))  # Output: [2, 4]
    print(two_sum([3, 3], 6))  # Output: [3, 3]
