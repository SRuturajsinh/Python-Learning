"""
Dictionary Searching

We can check whether a key or value
exists in a dictionary.
"""

student = {
    "name": "Ruturaj",
    "age": 20,
    "course": "Python"
}


# Checking if a key exists
print("name" in student)
print("city" in student)


# Checking if a key does NOT exist
print("city" not in student)


# Checking if a value exists
# if value exists in any key it will return True
print("Ruturaj" in student.values())
print("Java" in student.values())


# Using if
if "course" in student:
    print("Course exists")

if "city" not in student:
    print("City does not exist")