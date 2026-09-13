"""
Nested Dictionaries

A nested dictionary is a dictionary inside another dictionary.

A dictionary can store another dictionary as its value.

We'll learn:

1. Creating a nested dictionary
2. Accessing an inner dictionary
3. Accessing values from an inner dictionary
4. Changing values inside a nested dictionary
"""
student = {
    "student1": {
        "name": "Ruturaj",
        "age": 20,
        "course": "Python"
    },
    "student2": {
        "name": "Rahul",
        "age": 21,
        "course": "Java"
    }
}

# Print the complete dictionary
print(student)

# Access one student's dictionary
print(student["student1"])

# Access individual values
print(student["student1"]["name"])
print(student["student1"]["age"])
print(student["student2"]["course"])

# Change a nested value
student["student1"]["age"] = 22

print(student["student1"])