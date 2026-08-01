"""
This program demonstrates string manipulation methods in Python.
"""

# -------------------------
# f-Strings
# -------------------------

name = "Ruturajsinh"

print(f"My name is {name} and I am learning Python.")
# f-strings allow variables to be inserted directly into a string.
# If you forget the 'f' before the string, the variables will not be replaced.

# String Concatenation
first_name = "Ruturajsinh"
last_name = "Sarvaiya"

print(f"{first_name} {last_name}")
# Output: Ruturajsinh Sarvaiya

# Multiple variables
age = 19

print(f"My name is {first_name} {last_name} and I am {age} years old.")
# Output: My name is Ruturajsinh Sarvaiya and I am 19 years old.

# -------------------------
# String Case Methods
# -------------------------

name = "hello welcome to my python programming journey"

print(name.upper())
# Converts all the letters into uppercase
# HELLO WELCOME TO MY PYTHON PROGRAMING JOURNEY

print(name.lower())
# Converts all the letters into lowercase
# hello welcome to my python programing journey

print(name.title())
# Converts the first letter of each word into uppercase
# Hello Welcome To My Python Programing Journey

print(name.capitalize())
# Hello welcome to my python programing journey
# Converts only the first letter of the string to uppercase.

# -------------------------
# String Cleaning Methods
# -------------------------

name = "      hello welcome to my python programming journey      "

print(name)
# Prints the string with spaces.

print(name.strip())
# Removes spaces from the beginning and end of the string.

name = "hello welcome to my python programming journey"

print(name.strip("hello"))
# Removes the characters h, e, l, and o from the beginning and end.
# It does NOT remove the exact word "hello".

# -------------------------
# String Searching Methods
# -------------------------

message = "I love Python programming with Python"

# Check if text exists
print("Python" in message)          # True
print(message.startswith("I"))      # True
print(message.endswith("Python"))   # True

# Find position and count
print(message.find("Python"))       # 7
print(message.count("Python"))      # 2

# Replace text
new_message = message.replace("Python", "JavaScript")
print(new_message)
# Output: I love JavaScript programming with JavaScript
