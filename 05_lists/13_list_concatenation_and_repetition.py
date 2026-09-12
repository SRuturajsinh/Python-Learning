"""
List Concatenation and Repetition

We'll learn:

1. Joining two lists using +
2. Repeating a list using *
3. Adding lists without changing the original lists
"""

# 1. List Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2

print(combined)       # [1, 2, 3, 4, 5, 6]


# 2. List Repetition
numbers = [1, 2, 3]

repeated = numbers * 3 
print(repeated)       # [1, 2, 3, 1, 2, 3, 1, 2, 3]