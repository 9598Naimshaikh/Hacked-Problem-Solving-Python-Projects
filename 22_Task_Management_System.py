# Todo: Question--22 --Task Management System

# You are tasked with implementing a simple task management system. You need to create a Task class to represent
# tasks. Each task has a title, description, and a status (whether it's completed or not).

# Write a Python program that includes the following:

# 1. Create a Task class with attributes for title, description, and status. The status should be a boolean value (
# True for completed, False for incomplete).

# 2. Implement a method in the Task class to mark a task as completed.

# 3 Implement a method in the Task class to display the task details, including its title, description, and status.

# 4. Create a list to store instances of the Task class.

# 5. Implement a menu-driven program that allows the user to:
#    (i).   Add a new task to the list.
#    (ii).  Mark a task as completed.
#    (iii). View the list of tasks along with their details.
#    (iv).  Quit the program.

# 6. Use a loop to repeatedly display the menu and process user input until the user chooses to quit.

# Here's a simplified menu structure you can use as a guide:
"""
Task Management System
-----------------------
1. Add Task
2. Mark Task as Completed
3. View Tasks
4. Quit

Enter your choice:
"""


class Task:
    def __init__(self, title, description):
        self._title = title
        self._description = description
        self._completed = False

    def __str__(self):
        status = "Completed" if self._completed else "Uncompleted"
        return f"Title: {self._title}\nDescription: {status}"


task1 = Task("helo", "Coder life is the best")
print(task1)


