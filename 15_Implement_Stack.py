# 15: Implement a Stack
#
# Implement a basic stack data structure in Python. A stack is a collection of elements that supports two main
# operations: push, which adds an element to the top of the stack, and pop, which removes the top element from the
# stack. You should also implement a method called peek to view the top element without removing it and a method
# called is_empty to check if the stack is empty.
#
# Your task is to implement the Stack class with the following methods:
#
# push(element): Adds the given element to the top of the stack.
# pop(): Removes and returns the top element from the stack. If the stack is empty, return None.
# peek(): Returns the top element of the stack without removing it. If the stack is empty, return None.
# is_empty(): Returns True if the stack is empty, otherwise returns False.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):
        """Adds the given element to the top of the stack."""
        self.items.append(element)
        print(f'Element: {element} push successfully.!')

    def pop(self):
        """ Removes and returns the top element from the stack. If the stack is empty, return None."""
        return self.items.pop()

    def peek(self):
        """ Returns the top element of the stack without removing it. If the stack is empty, return None."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        """Returns True if the stack is empty, otherwise returns False."""
        return len(self.items) == 0


stack = Stack()
stack.push(50)
stack.push(40)
stack.push(30)

print(stack.pop())  # Output should be 30
print(stack.peek())  # Output should be 20
print(stack.is_empty())  # Output should be False
