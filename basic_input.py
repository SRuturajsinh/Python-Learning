"""
This program demonstrates basic Python concepts.
"""

print("Hello, World!")

# Variables
name = "ruturajsinh"
age = 21

print(name)
print(age)

print("Hello, my name is " + name + " and I am", age, "years old.")
print("Hi, my name is", name)

# Different ways to print variables
print(name, age)  # Using comma
print(name + " " + str(age))  # Convert age to string for concatenation
print(name + str(age))  # Without space
print(name + " " + str(age))

print(name + " is", age)

# Reassign variables
name = "hinaba"
print(name)

print(name, age)

age = 17
print("Age of", name, "is", age)

# Type conversion
a = "10"
print(a)

a = int("10") + 10
print(a)
print(10, "is the value of a")

print(str(a) + " string")
print(a, "string")

print(str(int("10")) + " hlw")
print(int(a), "hi")
print(10, "hlw")
print("hlw" + "hlw")

# Data types
result = 10 / 2
result = 10 / 10
result = 10 // 2
result = 10 // 10  # / returns float, // performs floor division
print(result)
print(type(result))

# Single quotes
first = 'Python'
first = 'it\'s python'

# Double quotes
second = "Python"
second = "it's python"

# Triple quotes for multiple lines
paragraph = """This is
a multi-line
string"""

print(first)
print(second)
print(paragraph)

# String operations
first_name = "John"
last_name = "Doe"

# Concatenation
full_name = first_name + " " + last_name
print(full_name)  # John Doe

# Repetition
stars = "1"
print(stars * 5)

# Length of strings
message = "Hello"
print(len(message))

empty = ""
print(len(empty))

# Wrong (will cause TypeError)
# result = "Age: " + 25

# Correct - convert number to string
result = "Age: " + str(25)
print(result)

# String repetition
word = " python "
print(word * 3)