# 04_lists_and_tuples.py

# --- Lists ---
# A list is a mutable (changeable) collection of items
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print("First fruit:", fruits[0])  # apple

# Modifying elements
fruits[1] = "blueberry"
print("Modified list:", fruits)

# Adding elements
fruits.append("orange")
print("After append:", fruits)

# Removing elements
fruits.remove("cherry")
print("After removal:", fruits)

# Looping through a list
for fruit in fruits:
    print("Fruit:", fruit)

# List slicing
print("First two fruits:", fruits[:2])

# --- Tuples ---
# A tuple is like a list, but immutable (unchangeable

