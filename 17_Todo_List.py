# Todo: Question: Implement a To-Do List
#   Create a simple command-line to-do list program in Python. Your program should allow users to perform the following
#   operations:
#       1. Add a task: Users should be able to add tasks to their to-do list.
#       2. View tasks: Users should be able to view their current to-do list.
#       3. Mark a task as done: Users should be able to mark tasks as done or completed.
#       4. Delete a task: Users should be able to delete tasks from their to-do list.
#   You should implement these operations using functions and a list to store the tasks.
#   Here's a sample interaction with the program:

"""
To-Do List Program
-------------------

1. Add a task
2. View tasks
3. Mark a task as done
4. Delete a task
5. Quit

Enter your choice: 1
Enter the task: Buy groceries
Task added successfully!

Enter your choice: 1
Enter the task: Clean the house
Task added successfully!

Enter your choice: 2
To-Do List:
1. Buy groceries
2. Clean the house

Enter your choice: 3
Enter the task number to mark as done: 1
Task 'Buy groceries' marked as done!

Enter your choice: 4
Enter the task number to delete: 2
Task 'Clean the house' deleted!

Enter your choice: 2
To-Do List:
1. Buy groceries

Enter your choice: 5
Goodbye!
"""

Todo_List = []


def add_task():
    task = input('Enter a task which do you want to add ✍️ $: ')
    Todo_List.append(task)
    print('Task added successfully!🎉🎊')
    print("------------------------")


def view_task():
    for index, task in enumerate(Todo_List, start=1):
        print(f'{index}. {task}')

    print("------------------------")


def mark_task_as_done():
    task_num = int(input("Enter the task number to mark as done: "))
    for index, task in enumerate(Todo_List, start=1):
        if task_num == index:
            print(f'Task {task!r} marked as done!✅')

    print("------------------------")


def delete_task():
    task_num = int(input("Enter a task number to delete: "))
    for index, task in enumerate(Todo_List, start=1):
        if task_num == index:
            Todo_List.remove(task)
            print(f'Task {task!r} Deleted!❌')

    print("------------------------")


if __name__ == "__main__":
    print('To-Do List Program')
    while True:
        try:
            print('-------------------')
            options = ["Add a task", "View tasks", "Mark a task as done", "Delete a task", "Quit"]
            for index, opt in enumerate(options, start=1):
                print(f"{index}. {opt}")
            print()

            user_choice = int(input('Enter choice $$: '))

            if user_choice == 1:
                add_task()

            elif user_choice == 2:
                view_task()

            elif user_choice == 3:
                mark_task_as_done()

            elif user_choice == 4:
                delete_task()

            elif user_choice == 5:
                print('GoodBye.!')
                break

            user_doitAgain = input("What do you want to play again ? (Yes/No)$: ").lower()
            if user_doitAgain == 'no' or user_doitAgain == 'n':
                print("Thanks for using Todo Program.")
                print("Good Byy.!👋")
                quit()

        except Exception as e:
            print(f"Error: {e}")
