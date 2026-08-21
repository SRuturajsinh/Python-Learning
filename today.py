"""
List Copying and References

This program demonstrates:

1. Assignment (=)
2. copy()
3. list()
4. Changing copied lists
5. Comparing lists
"""

# ==================================================
# 1. Assignment
# ==================================================

numbers = [1, 2, 3, 4, 5]

# Both variables refer to the same list.
a = numbers

print("Original list:", numbers)
print("A:", a)

# Changing 'a' also changes 'numbers'
a[0] = 100

print("After changing A:")
print("Original list:", numbers)
print("A:", a)


# ==================================================
# 2. copy()
# ==================================================

numbers = [1, 2, 3, 4, 5]

# copy() creates a separate copy of the list.
b = numbers.copy()
print("\nbefore changing b:",b)
b[0] = 100

print("\nUsing copy():")
print("Original list:", numbers)
print("B:", b)


# ==================================================
# 3. list()
# ==================================================

numbers = [1, 2, 3, 4, 5]

# list() creates a separate copy of the list.
c = list(numbers)

c[0] = 100

print("\nUsing list():")
print("Original list:", numbers)
print("C:", c)


# ==================================================
# 4. Comparing Lists
# ==================================================

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [4, 5, 6]

print("\nComparing lists:")

print(list1 == list2)  # True
print(list1 == list3)  # False