# 07_modules_and_packages.py

# --- Importing built-in modules ---
import math
import random

print("Square root of 16 is:", math.sqrt(16))
print("Random number between 1 and 10:", random.randint(1, 10))

# --- Importing specific functions from a module ---
from math import pi, ceil

print("Value of pi:", pi)
print("Ceiling of 3.2:", ceil(3.2))

# --- Creating a simple custom module (saved as my_module.py) ---
# # Content of my_module.py
# def greet(name):
#     return f"Hello, {name}!"

# def add(a, b):
#     return a + b

# --- Importing and using the custom module ---
import my_module

print(my_module.greet("Brian"))
print("Sum:", my_module.add(3, 4))

# --- Python Package Structure Example (create a folder named 'mypackage') ---
# Folder structure:
# mypackage/
# ├── __init__.py
# ├── math_ops.py
# └── greetings.py

# # Contents of math_ops.py
# def multiply(a, b):
#     return a * b

# # Contents of greetings.py
# def say_hi():
#     return "Hi there!"

# # Contents of __init__.py
# from .math_ops import multiply
# from .greetings import say_hi

# --- Using the package (assuming it's installed or in the same directory) ---
# from mypackage import multiply, say_hi
# print(multiply(3, 5))
# print(say_hi())

