"""
Dictionary with Lists

A dictionary can store a list as its value.

We'll learn:

1. Storing lists inside a dictionary
2. Accessing a list from a dictionary
3. Accessing individual elements from the list
4. Modifying a list inside a dictionary
5. Looping through a list stored in a dictionary
"""
student = {
    "name": "Ruturaj",
    "subjects": ["Python", "Math", "AI"],
    "marks": [85, 90, 88]
}


# Accessing a list

print(student["subjects"])


# Accessing an individual element

print(student["subjects"][0])
print(student["marks"][1])


# Modifying a list inside the dictionary

student["subjects"].append("English")

print(student["subjects"])


# Changing an element

student["marks"][0] = 95

print(student["marks"])


# Looping through a list stored in the dictionary

for subject in student["subjects"]:
    print(subject)