# LinkedIn Learning Python course by Joe Marini
# Working with modules of code

# import the math module, which contains features for working with mathematics
import math
print("The square root of 16 is", math.sqrt(16))

# import a specific part of the module so you can refer to it more easily
from math import pi as pie
print(f"Pi value is : {pie}")

# import a module and give it a different name
import random as r
print(r.randint(200,300))

# the math module contains lots of pre-built functions


# in addition to functions, some modules contain useful constants 


# Generate a random number between 100 and 200


# try some of the math functions for yourself here:

# Use the 3rd party tabulate module to print tabulated data:
import tabulate
# from tabulate import tabulate

# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]

print('\n')
print(
  tabulate.tabulate(data, headers='firstrow', tablefmt='fancy_grid')
)

# Create a formatted table
