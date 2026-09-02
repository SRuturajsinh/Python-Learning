"""
Nested List Operations

A nested list is a list that contains other lists.

In this program, we will learn how to:
1. Access elements
2. Modify elements
3. Add elements
4. Remove elements
5. Loop through nested lists
6. Find the sum of each row
7. Find the largest value in each row
8. Find the smallest value in each row
"""

# A nested list
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]


# --------------------------------------------------
# 1. Accessing Elements
# --------------------------------------------------

print(numbers[0])       # First inner list
print(numbers[1][2])   # Third element of second list


# --------------------------------------------------
# 2. Modifying Elements
# --------------------------------------------------

numbers[0][1] = 25

print(numbers)


# --------------------------------------------------
# 3. Adding Elements
# --------------------------------------------------

numbers[0].append(35)

print(numbers)


# --------------------------------------------------
# 4. Removing Elements
# --------------------------------------------------

numbers[1].remove(50)

print(numbers)


# --------------------------------------------------
# 5. Looping Through a Nested List
# --------------------------------------------------

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j])


# --------------------------------------------------
# 6. Finding the Sum of Each Row
# --------------------------------------------------

for i in range(len(numbers)):
    total = 0

    for j in range(len(numbers[i])):
        total += numbers[i][j]

    print("Sum:", total)


# --------------------------------------------------
# 7. Finding the Largest Value in Each Row
# --------------------------------------------------

for i in range(len(numbers)):
    largest = numbers[i][0]

    for j in range(len(numbers[i])):
        if numbers[i][j] > largest:
            largest = numbers[i][j]

    print("Largest:", largest)


# --------------------------------------------------
# 8. Finding the Smallest Value in Each Row
# --------------------------------------------------

for i in range(len(numbers)):
    smallest = numbers[i][0]

    for j in range(len(numbers[i])):
        if numbers[i][j] < smallest:
            smallest = numbers[i][j]

    print("Smallest:", smallest)
