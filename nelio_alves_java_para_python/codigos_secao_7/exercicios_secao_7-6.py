# Exercise 6 - Section 7.

# This program is designed to add and remove products.

# Definition of Product class.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Method to perform the calculation of the price from all products in stock.
    def total_stock_value(self):
        return self.price * self.quantity
    
    # Method to increase products in stock.
    def add_products(self, quantity):
        self.quantity += quantity

    # Method to remove products from the stock.
    def remove_products(self, quantity):
        self.quantity -= quantity
    # Custom string representation of the object.
    def __str__(self):
        return f"Product {self.name}, Individual price: $ {self.price}, Total in stock: $ {self.total_stock_value():.2f}"

# --- Main program starts here ---

# Welcome message and instructions.
print("Stock Control")
print()
print("Enter product data:")

# Entering product data:
name = input("Name: ")
price = float(input("Price "))
quantity = int(input("Quantity in stock: "))
product = Product(name, price, quantity) # Creating the product object.

# First data output.
print("Product data:")
print(product)

# New data input, adding more products.
print()
quantity = int(input("Enter the number of products to be added in stock: "))
product.add_products(quantity)
print("Updated product data:")
print(product)

# New data input, removing products.
print()
quantity = int(input("Enter the number of products to be removed from stock: "))
product.remove_products(quantity)
print("Updated product data:")
print(product)

