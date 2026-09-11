"""
We'll learn:

Assigning list elements to variables
Unpacking a list
Using * to collect multiple elements
Unpacking while passing values around
Common mistakes with unpacking
"""

nums = [1, 2, 3]

# We can assign elements of a list to separate variables.

a, b, c = nums

"""
Important:
We normally need the same number of variables as elements
in the list when using basic unpacking.

No more variables:
a, b, c, d = nums  # Error

No fewer variables:
a, b = nums        # Error
"""

print(a)  # 1
print(b)  # 2
print(c)  # 3