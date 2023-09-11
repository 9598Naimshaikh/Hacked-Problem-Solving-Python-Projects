# 13 - Employee Management System

# Create a Python program for managing employee records. Implement two classes: `Employee` and `EmployeeManager`.
# 1. `Employee Class`:
#    Attributes:
#       Employee ID (integer)
#       First Name (string)
#       Last Name (string)
#       Salary (float)

# 2. `EmployeeManager` Class:
#     Attributes:
#         employees (a list to store Employee objects)
#     Methods:
#         add_employee(self, employee: Employee): Add an employee to the list of employees.
#         remove_employee(self, employee_id: int): Remove an employee from the list based on their ID.
#         get_employee(self, employee_id: int) -> Employee: Retrieve an employee's details based on their ID.
#         get_all_employees(self) -> List[Employee]: Retrieve a list of all employees.
#         get_total_salary(self) -> float: Calculate and return the total salary of all employees.


class Employee:
    def __init__(self, emp_id, f_name, l_name, salary):
        self.emp_id = emp_id
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        """ Add an employee to the list of employees"""
        self.employees.append(employee)
        print('Employee has been added to successfully.!')

    def remove_employee(self, emp_id: int):
        """Remove an employee from the list based on their ID."""
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                print(f'Employee: {emp_id} removed successfully.!')
                return
        print(f'Employee: {emp_id} is not available.!')

    def get_employee(self, emp_id: int):
        """Retrieve an employee's details based on their ID."""
        for emp_details in self.employees:
            if emp_details.emp_id == emp_id:
                return f"Employee ID: {emp_details.emp_id}, Name: {emp_details.f_name} {emp_details.l_name}, Salary: {emp_details.salary}"
        return f'Employee {emp_id} Not Found.!'

    def get_all_employees(self):
        """Retrieve a list of all employees."""
        all_employees = [emp.f_name for emp in self.employees]
        print(f'All Employees: {all_employees}')


emp1 = Employee(9090, 'Naim', 'Shaikh', 30000.00)
emp2 = Employee(9080, 'Harish', 'Ali Khan', 23000.00)

manager = EmployeeManager()

manager.add_employee(emp1)
manager.add_employee(emp2)

manager.remove_employee(9090)

print(manager.get_employee(9080))
print(manager.get_employee(2332))

manager.get_all_employees()