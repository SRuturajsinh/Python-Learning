"""
Looping Through Lists

This program demonstrates:
1. Looping directly through a list
2. Using list indexes
3. Using len()
4. Using range()
"""

# ==========================================
# Looping Directly Through a List
# ==========================================

fruits = ["apple", "banana", "cherry"]

# Print every element of the list
for fruit in fruits:
    print(fruit)


# ==========================================
# Looping Using Index
# ==========================================

# range() generates index numbers
for i in range(3):
    print(fruits[i])


# ==========================================
# Length of a List
# ==========================================

print("Length of list:", len(fruits))


# ==========================================
# Looping Using len() and range()
# ==========================================

# len() gives the number of elements in the list
# range() generates indexes from 0 to length - 1

for i in range(len(fruits)):
    print(i, fruits[i])


# ==========================================
# Working With a Number List
# ==========================================

numbers = [1, 4, 3, 2, 5, 7, 6, 8]

# Print every number in the list
for number in numbers:
    print(number)


# Print numbers using their indexes
for i in range(len(numbers)):
    print(i, numbers[i])
