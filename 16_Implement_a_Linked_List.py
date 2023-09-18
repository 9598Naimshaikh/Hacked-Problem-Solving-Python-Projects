# 16 - Implement a Linked List

# Implement a basic singly linked list data structure in Python. A linked list is a collection of elements where each
# element points to the next element in the sequence, forming a chain. You should implement the following
# functionalities for your linked list:
#
# append(data): Adds an element with the given data to the end of the linked list.
# prepend(data): Adds an element with the given data to the beginning of the linked list.
# delete(data): Deletes the first occurrence of an element with the given data from the linked list.
# display(): Displays all elements in the linked list.

# Your task is to implement the LinkedList class with the mentioned methods.

class LinkedList:
    def __init__(self):
        self.linked_list = []

    def append(self, data):
        """appends an element to the end of the linked list."""
        self.linked_list.append(data)
        print("Append Success.!")

    def prepend(self, data):
        """inserts an element at the beginning of the linked list."""
        self.linked_list.insert(0, data)
        print("Prepend Success.!")

    def delete(self, data):
        """removes the first occurrence of an element with the given data from the linked list."""
        self.linked_list.remove(data)
        print('Delete Success.!')

    def display(self):
        """ Displays all elements in the linked list."""
        print(f'Output: {self.linked_list}')


my_list = LinkedList()

my_list.append(10)
my_list.append(34)
my_list.prepend(2)
my_list.delete(2)
my_list.display()
