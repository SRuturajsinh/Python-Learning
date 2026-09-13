"""
Adding and Changing Dictionary Data

We can add new key-value pairs
and change existing values.
"""

student = {
    "name" : "Ruturajsinh",
    "age" : 21,
    "course" : "Advance Python"
}

# Main Dictionary
print (student)

# Adding a new key-value pair
student["city"] = "Vadodara"
print(student)

# Changing an existing value
student["age"] = 19
print(student)

# Deleting a key-value pair
del student["course"]
print(student)