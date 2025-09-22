# Exercise 5 - Section 7.

# This program converts the United States Dollars to Brazilian Reais, and applies the Brazilian IOF tax.

# Definition of Converter class.
class Converter:
    # Constant representing the fixed IOF value
    IOF = 0.06

    def __init__(self, value, amount):
        self.value = value
        self.amount = amount

    # Method to perform the currency conversion including IOF.
    def calculator(self):
        return self.value * self.amount * (1.0 + Converter.IOF)
    
    # Method to calculate the IOF tax amount separately.
    def iof_value(self):
        return self.calculator() - (self.value * self.amount)
            
# --- Main program starts here ---

# Welcome message and instructions.
print("Dollar to Real Converter")
print()
print("The Brazilian IOF tax will be automatically applied")

# Getting user input.
dollar_value = float(input("Current dollar exchange rate: "))
dollar_amount = float(input("How many dollars will be bought? "))
converter = Converter(dollar_value, dollar_amount) # Creating the converter object.

# Data output.
converted_value = converter.calculator()
converted_iof = converter.iof_value()
print(f"Amount to be paid in BRL: R$ {converted_value:.2f}")
print(f"IOF total value for this operation in BRL: {converted_iof:.2f}")

# End of program.
print("--------------------------------------------")
print("End of program.")
