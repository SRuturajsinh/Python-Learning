"""
Dictionary Comprehension

Dictionary comprehension allows us to create
a dictionary using a single line of code.

We'll learn:

1. Basic dictionary comprehension
2. Creating key-value pairs
3. Using conditions
"""

# Basic dictionary comprehension

squares = {number: number * number for number in range(1, 6)}

print(squares)