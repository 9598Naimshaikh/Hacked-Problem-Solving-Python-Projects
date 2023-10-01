# Question 21: Find the Second Largest Number

# Write a Python function called find_second_largest(numbers) that takes a list of integers as input and returns the
# second largest number in the list.

# Example:
# print(find_second_largest([1, 2, 3, 4, 5]))  # Should print 4


def find_second_largest_num(number_list):
    if len(number_list) < 2:
        print('Sorry! No second largest number.!')

    number_list.sort()
    return number_list[-2]


if __name__ == "__main__":
    print(find_second_largest_num([2, 4, 6, 2, 4, 9]))
    print(find_second_largest_num([3, 1, 4, 5, 23, 43]))