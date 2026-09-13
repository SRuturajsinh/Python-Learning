
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