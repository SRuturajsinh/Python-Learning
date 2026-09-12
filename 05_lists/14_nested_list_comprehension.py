"""
Nested List Comprehension

We'll learn how to use list comprehension
with nested lists.
"""

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using normal nested loops
result = []

for row in numbers:
    for number in row:
        result.append(number)

print(result)#[1, 2, 3, 4, 5, 6, 7, 8, 9]