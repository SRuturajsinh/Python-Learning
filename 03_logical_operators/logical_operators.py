"""
This program demonstrates the logical operators:
and, or, and not in Python.
"""
# AND: Both must be True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# OR: At least one must be True  
print(True or False)    # True
print(False or False)   # False

# NOT: Flips the value
print(not True)         # False
print(not False)        # True

"""
The same examples are shown again with descriptive text
to make the output easier to understand.
"""

# AND: Both conditions must be True
print("True and True:", True and True)
print("True and False:", True and False)
print("False and False:", False and False)

print()

# OR: At least one condition must be True
print("True or False:", True or False)
print("False or False:", False or False)

print()

# NOT: Reverses the Boolean value
print("not True:", not True)
print("not False:", not False)
