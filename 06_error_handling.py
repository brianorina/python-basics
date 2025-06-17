# 09_error_handling.py

# --- Basic try-except ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# --- Catching multiple exceptions ---
try:
    num = int("ten")
except ValueError:
    print("That's not a valid integer.")
except Exception as e:
    print("An unexpected error occurred:", e)

# --- Using else ---
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("You entered:", age)

# --- Using finally ---
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block always runs, whether an error occurred or not.")

# --- Raising exceptions manually ---
def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

try:
    print(divide(10, 2))
    print(divide(5, 0))
except ValueError as ve:
    print("Caught an error:", ve)

