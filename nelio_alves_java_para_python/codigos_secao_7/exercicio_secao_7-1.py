# Exercise 1 - Section 7.

# First contact with object-oriented programmin and class creation in Python.
# This program compares the area of two triangles and determines which one is larger.

import math # Importing the math module to access mathematical functions.

# Defining the Triangle class.
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    # Method to calculate the area, using Heron's formula.        
    def area(self):
        p = (self.a + self.b + self.c) / 2.0
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

# --- Main program starts here ---

# Welcome message and instructions.
print("Triangle Area Comparator")
print()
print("Enter the measurements for each triangle:")

# Input for Triangle X.
print("Triangle X")
a1 = float(input("Side a: "))
b1 = float(input("Side b: "))
c1 = float(input("Side c: "))
print()
x = Triangle(a1, b1, c1) # Creating Triangle X object.

# Input for Triangle Y.
print("Triangle Y")
a2 = float(input("Side a: "))
b2 = float(input("Side b: "))
c2 = float(input("Side c: "))
print()
y = Triangle(a2, b2, c2) # Creating Triangle Y object.

# Calculating the area of each triangle.
area_x = x.area()
area_y = y.area()

# Displaying the areas.
print(f"Triangle X area is: {area_x:.2f}")
print(f"Triangle Y area is: {area_y:.2f}")
print()

# Comparing the areas.
if (area_x > area_y):
    print("Triangle X has the larger area.")
elif (area_x < area_y):
    print("Triangle Y has the larger area.")
else:
    print("Both triangles have the same area.")

# End of program.
print("------------------------------")
print("Program finished.")