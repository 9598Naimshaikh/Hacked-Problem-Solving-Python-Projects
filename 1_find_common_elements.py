# Problem: Find Common Elements

# Write a Python function that finds and returns the common elements from two lists.
# The order of elements in the output list should be the same as in the original lists.


def find_common_elements(l1, l2):
    count_common_elements = []
    for i in l1:
        for j in l2:
            if i == j:
                count_common_elements.append(i)
    count_elements = set(count_common_elements)
    count_common_elements = list(count_elements)

    return count_common_elements


if __name__ == '__main__':
    l1, l2 = [2, 3, 4, 6, 8], [5, 2, 4, 7, 6, 4, 3]
    print(find_common_elements(l1, l2))
    print(find_common_elements([2, 3, 4, 5], [5, 4, 9, 7, 5]))
