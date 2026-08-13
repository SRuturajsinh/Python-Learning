"""
Introduction to Lists

Lists are used to store multiple items in a single variable.
Lists are ordered collections of items that can be accessed.

Basic list creation
"""

# Empty list
my_list = []
print(my_list)

type(my_list) # <class 'list'>

# List with elements
fruits_list = ["apple", "banana", "cherry"] # strings
number_list = [1, 2, 3, 4, 5]               # integers
boolean_list = [True, False, True]          # booleans       
mixed_list = ["apple", 1, True, 3.14]       # mixed data types

print(fruits_list)
print(number_list)
print(boolean_list)
print(mixed_list)

# List with different data types
name = "Ruturajsinh"
age = 19
gender = "Male"
have_id = True
user_info = [name,age,gender,have_id]
print(f"User information: {user_info}")