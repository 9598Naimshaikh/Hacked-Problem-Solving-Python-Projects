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
        self.title = title
        self.description = description
        self.status = False

    def mark_completed(self):
        self.status = True

    def display_task_details(self):
        status = "Completed" if self.status else "Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {status}"


# Create a list to store instances of the Task class
tasks = []


def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = Task(title, description)
    tasks.append(task)
    print("Task added successfully!")


def mark_completed_task():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task.title}")
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index].mark_completed()
            print(f"{tasks[task_index].title} has been marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


def view_tasks():
    print("\nTask List:")
    for i, task in enumerate(tasks):
        print(f"\nTask {i + 1}:\n{task.display_task_details()}")


while True:
    print("\nTask Management System")
    print("-----------------------")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        mark_completed_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Thank you for using the Task Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")
