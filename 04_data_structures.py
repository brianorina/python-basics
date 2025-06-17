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

# 05_dictionaries.py

# --- Dictionaries ---
# A dictionary is a collection of key-value pairs

# Creating a dictionary
person = {
    "name": "Brian",
    "age": 25,
    "location": "Spain"
}

# Accessing values
print("Name:", person["name"])
print("Age:", person.get("age"))

# Adding a new key-value pair
person["email"] = "brian@example.com"
print("Updated dictionary:", person)

# Updating a value
person["age"] = 26
print("After update:", person)

# Removing a key-value pair
del person["location"]
print("After deletion:", person)

# Looping through keys
for key in person:
    print("Key:", key, "→ Value:", person[key])

# Looping through items
for key, value in person.items():
    print(f"{key} = {value}")


# 06_conditions.py

# --- Basic if/else ---

age = 20

if age >= 18:
    print("You're an adult.")
else:
    print("You're a minor.")

# --- if/elif/else chain ---

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

# --- Logical operators ---

has_passport = True
has_ticket = False

if has_passport and has_ticket:
    print("You can board the plane.")
else:
    print("You can't board the plane.")

# --- Nested if ---

temperature = 25

if temperature > 20:
    if temperature < 30:
        print("Nice weather!")
    else:
        print("It's hot!")
else:
    print("It's cold.")
# 07_loops.py

# --- for loop ---

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Loop through a string
for letter in "Python":
    print("Letter:", letter)

# Loop using range()
for i in range(5):
    print("i =", i)

# Loop with start and end
for i in range(1, 6):
    print("Count:", i)

# --- while loop ---

count = 0
while count < 5:
    print("While loop count:", count)
    count += 1

# --- break statement ---
for num in range(10):
    if num == 5:
        break  # Exit loop early
    print("Break loop num:", num)

# --- continue statement ---
for num in range(5):
    if num == 2:
        continue  # Skip this iteration
    print("Continue loop num:", num)

# --- else with loops ---
for i in range(3):
    print("Loop iteration:", i)
else:
    print("Loop completed without break.")


