# 6. Find the Missing Number

# You are given a list of n-1 unique integers from 1 to n, and these integers are in random order. One number from 1
# to n is missing. Write a Python function to find and return the missing number.

# Write a function named find_missing_number that takes a list of integers as input and returns the missing integer.


def find_missing_num(nums):
    n = len(nums) + 1
    exact_num = (n * (n + 1)) // 2
    # print(exact_num)
    total_num = sum(nums)
    # print(total_num)
    missing_num = exact_num - total_num
    return missing_num


if __name__ == '__main__':
    print(find_missing_num([1, 2, 3, 4, 5, 6, 8]))
