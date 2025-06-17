# 02_loops_and_conditions.py

# --- Conditional Statements (if, elif, else) ---
age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")

# --- For Loops ---
# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Looping with range()
for i in range(5):
    print("Number:", i)  # 0 to 4

# --- While Loops ---
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# --- Using break and continue ---
# break = exit the loop early
# continue = skip the current iteration

for number in range(1, 6):
    if number == 3:
        continue  # skip printing 3
    if number == 5:
        break     # stop the loop at 5
    print("Processed number:", number)

# Output will be: 1, 2, 4

