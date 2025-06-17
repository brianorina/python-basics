# 08_file_handling.py

# --- Writing to a file ---
with open("example.txt", "w") as file:
    file.write("Hello, this is a text file.\n")
    file.write("We are learning file handling in Python.\n")

print("File written successfully.")

# --- Reading from a file ---
with open("example.txt", "r") as file:
    content = file.read()
    print("\n--- File Content ---")
    print(content)

# --- Reading line by line ---
with open("example.txt", "r") as file:
    print("\n--- Reading line by line ---")
    for line in file:
        print(line.strip())

# --- Appending to a file ---
with open("example.txt", "a") as file:
    file.write("This line is added using append mode.\n")

# --- Check updated content ---
with open("example.txt", "r") as file:
    print("\n--- Updated Content ---")
    print(file.read())

