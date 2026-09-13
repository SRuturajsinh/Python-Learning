"""
Looping Through Dictionaries

We can loop through:
1. Keys
2. Values
3. Key-value pairs
"""

student = {
    "name": "Ruturaj",
    "age": 20,
    "course": "Python"
}

# 1. Loop through keys
for key in student:
    print(key)

# 2. Loop through values
for value in student.values():
    print(value)

# 3. Loop through key-value pairs
for key, value in student.items():
    print(key,":", value)