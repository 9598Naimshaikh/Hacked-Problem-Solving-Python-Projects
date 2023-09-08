# Question 8: Bank Account

# Create a Python class called BankAccount that represents a basic bank account. The class should have the following
# features:

# 1. Initialize the account with an account holder's name and an initial balance.
# 2. Implement methods to deposit money into the account and withdraw money from the account.
# 3. Implement a method to check the current balance of the account.

# Write the BankAccount class with the following methods:

class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit_money(self, money):
        self._balance += money
        print(f'{money}Rs. successfully Deposit in your account.!')

    def withdraw_money(self, money):
        self._balance -= money
        print(f'{money}Rs. successfully withdraw in your account.!')

    def show_balance(self):
        return self._balance


b1 = BankAccount('Naim', 1000)

b1.deposit_money(500)
print(b1.show_balance())
b1.withdraw_money(1000)
print(b1.show_balance())
# print(b1._balance)
