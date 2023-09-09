# 10: Employee Management System

# Create a Python class called Employee that represents an employee with the following attributes:

# (i).  Employee ID
# (ii). First Name
# (iii).Last Name
# (iv). Email Address
# (v).  Salary

# Implement a Company class that represents a company containing a collection of employees. The Company class should
# have the following features:

# 1. Initialize an empty collection of employees.
# 2. Implement a method to add an employee to the company.
# 3. Implement a method to remove an employee from the company.
# 4. Implement a method to search for an employee by Employee ID and return their details (ID, first name, last name, email, and salary).
# 5. Implement a method to calculate the total salary of all employees in the company.


class Employee:
    def __init__(self, id, f_name, l_name, email_add, salary):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.email_add = email_add
        self.salary = salary


class Company:
    def __init__(self):
        self.employees = []
        self.no_of_emp = 0

    def add_employee(self, employee):
        self.employees.append(employee)
        self.no_of_emp += 1
        print(f'Employee {self.no_of_emp} has been added successfully.!')

    def remove_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                self.employees.remove(emp1)
                print(f'Employee: {emp_id} removed successfully.!')
            return
        print(f'Employee ID: {emp_id} Not Found.!')

    def search_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                print(
                    f'Employee ID: {emp.id}, First Name: {emp.f_name}, Last Name: {emp.l_name}, Email: {emp.email_add}, Salary: {emp.salary}')
                return
        print(f'Employee ID: {emp_id} not found.!')

    def total_salary(self):
        total_salary = 0.0
        for emp in self.employees:
            total_salary += emp.salary
        print(f'Total Salary of All Employees: {total_salary}')


# Creating employee instances
emp1 = Employee(224, 'Naim', 'Shaikh', 'nn9412466@gmail.com', 20000)
emp2 = Employee(555, 'Sam', 'Shaikh', 'ss3434@gmail.com', 34343)

# Creating a company instance
comp1 = Company()

# Adding employees to the company
comp1.add_employee(emp1)
comp1.add_employee(emp2)

# Removing an employee by ID
# comp1.remove_employee(224)

# Searching for employees by ID
comp1.search_employee(224)
comp1.search_employee(555)


# Calculating and displaying the total salary
comp1.total_salary()





# if __name__ == '__main__':
#     print('...Welcome to Google Company...')
#     while True:
#         print('Option-----')
#         print('1. ADD EMPLOYEES \n2. REMOVE EMPLOYEES \n3. SEARCH EMPLOYEES \n4. CALCULATE THE ALL EMPLOYEES SALARY '
#               '\n5. QUIT THE PROGRAM \n')
#
#         user_choice = int(input('Enter choice (1,2,3,4,5) $: '))
#         if user_choice == 1:
#
#         break