# Exercise 2 - Section 7.

# This program calculates the area, perimeter and diagonal of a rectangle.

import math # Importing the math module to access mathematical functions.

# Defining the Rectangle class.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # Method to calculate the rectangle area.    
    def area(self):
        return self.width * self.height
    # Method to calculate the rectangle perimeter.    
    def perimeter(self):
        return 2 * (self.width + self.height)
    # Method to calculate the rectangle diagonal.    
    def diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)
    # Custom string representation of the object.
    def __str__(self):
        return f"Area: {self.area():.2f}\nPerimeter: {self.perimeter():.2f}\nDiagonal: {self.diagonal():.2f}"
    
# --- Main program starts here ---

# Welcome message and instructions.
print("Rectangle Analyser")
print()
print("Enter the rectangle width and height:")

# Getting user input for rectangle dimensions.
print()
width = float(input("Width: "))
height = float(input("Height: "))
rectangle = Rectangle(width, height) # Creating Rectangle object.

# Displaying results and ending the program.
print()
print(rectangle)
print("-----------------------")
print("End of program.")
