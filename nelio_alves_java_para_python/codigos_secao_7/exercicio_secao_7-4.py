# Exercise 4 - Section 7.

# This program calculates a student's final grade.
# If the score is greater than or equal to 60, the student is approved.

# Definition of Student class.
class Student:
    def __init__(self, name, first_quarter_grade, second_quarter_grade, third_quarter_grade):
        self.name = name
        self.first_quarter_grade = first_quarter_grade
        self.second_quarter_grade = second_quarter_grade
        self.third_quarter_grade = third_quarter_grade
        
    # Method to calculate the total grade.
    def grade_calculator(self):
        return self.first_quarter_grade + self.second_quarter_grade + self.third_quarter_grade
    
    # Method to check if student is approved.
    def pass_checker(self):
        final_grade = self.grade_calculator()
        if (final_grade >= 60):
            return True
        else:
            return False

# --- Main program starts here ---

# Welcome message and instructions.
print("Student Grade Evaluator")
print()
print("Enter student data:")

# Getting user input for student data.
print()
name = input("Enter student name: ")
first_quarter_grade = float(input("Enter first quarter grade: "))
second_quarter_grade = float(input("Enter second quarter grade: "))
third_quarter_grade = float(input("Enter third quarter grade: "))
student = Student(name, first_quarter_grade, second_quarter_grade, third_quarter_grade) # Creating student object.

# Checking pass/fail status with output messages.
final_grade = student.grade_calculator()
if (student.pass_checker()):
    print()
    print("Student Status:")
    print(f"{student.name} passed with a final grade of: {final_grade:.2f} points.")
else:
    missing = 60 - final_grade
    print()
    print("Student Status:")
    print(f"{student.name} failed with a final grade of: {final_grade:.2f} points.")
    print(f"Missing points: {missing:.2f} points.")

# End of program.
print("--------------------------------------------")
print("End of program.")
