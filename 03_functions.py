# 03_functions.py

# --- Built-in function example ---
print("Hello from a built-in function!")
length = len("Python")
print("Length of the word 'Python':", length)

# --- User-defined function ---
def greet(name):
    print(f"Hello, {name}!")

greet("Brian")  # Output: Hello, Brian!

# --- Function with return value ---
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)  # Output: 8

# --- Function with default parameter ---
def power(base, exponent=2):
    return base ** exponent

print("2 squared:", power(2))       # 4
print("2 to the power 3:", power(2, 3))  # 8

# --- Function with multiple return values ---
def get_name_and_age():
    return "Brian", 25

name, age = get_name_and_age()
print("Name:", name)
print("Age:", age)

