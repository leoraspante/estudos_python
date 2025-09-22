# Exercise 3 - Section 7.

# This program calculates the salary and applied taxes, returning net salary.

# Definition of Employee class.
class Employee:
    def __init__(self, name, gross_salary, tax):
        self.name = name
        self.gross_salary = gross_salary
        self.tax = tax

    # Method to calculate the net salary.
    def net_salary(self):
        return self.gross_salary - (self.gross_salary * self.tax / 100)
    
    # Method to apply a salary increase by percentage.
    def increase_salary(self, percentage):
        self.gross_salary += (self.gross_salary * percentage) / 100


# --- Main program starts here ---

# Welcome message and instructions.
print("Salary Calculator")
print()
print("Enter employee data:")

# Getting user input for employee data.
print()
name = input("Enter employee name: ")
gross_salary = float(input("Enter employee gross salary: "))
tax = float(input("Enter tax value: "))
employee = Employee(name, gross_salary, tax) # Creating Employee object.

# First data output.
print()
print(f"Employee name: {employee.name} - Salary: $ {employee.net_salary():.2f}")

# Getting user input for salary increase.
print("How much would you like to increase the salary (in %)?")
print()
percentage = float(input("Enter percentage: "))
employee.increase_salary(percentage)
    
# Second data output.
print()
print("Updated employee data")
print(f"Employee name: {employee.name} - Salary: $ {employee.net_salary():.2f}")

# Ending the program.
print("-----------------------")
print("End of program.")
