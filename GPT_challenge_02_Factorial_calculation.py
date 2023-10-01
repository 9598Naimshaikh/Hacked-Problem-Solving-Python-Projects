# Challenge 3: Factorial Calculation

# Write a Python function that calculates the factorial of a given non-negative integer. The factorial of a
# non-negative integer n is the product of all positive integers less than or equal to n.


# This code without recursion to find factorial number...

def factorial_num(number):
    if number < 0:
        return "Please enter positive number"
    elif number == 0:
        return 1
    factorial = 1
    for n in range(1, number+1):
        factorial *= n

    return factorial


if __name__ == "__main__":
    num = int(input("Enter number! which number do you want to find factorial number $: "))
    print(factorial_num(num))




# num = int(input('Enter a num: '))
#
# if num < 0:
#     print("Please enter a positive number")
# elif num == 0:
#     print(1)
# factorial = 1
# for n in range(1, num + 1):
#     factorial *= n
#
# print(factorial)
