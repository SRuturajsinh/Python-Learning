"""
You've learned creating, indexing, slicing, looping, and modifying lists.
Now learn how to check whether something exists in a list.
"""


# ==================================================
# in - Check if something exists in a list
# ==================================================

fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)    # True
print("mango" in fruits)    # False


# ==================================================
# not in - Check if something does not exist
# ==================================================

print("apple" not in fruits)    # False
print("mango" not in fruits)    # True


# ==================================================
# if + in - Check if something exists
# ==================================================

if "apple" in fruits:
    print("apple is in the list")
else:
    print("apple is not in the list")


if "mango" in fruits:
    print("mango is in the list")
else:
    print("mango is not in the list")


# ==================================================
# count() - Count how many times a value appears
# ==================================================

nums = [1, 2, 3, 4, 5, 4, 4, 3, 2, 1]

print(nums.count(4))    # 3
print(nums.count(3))    # 2
print(nums.count(1))    # 2


# ==================================================
# index() - Find the index of a value
# ==================================================

vehicles = ["car", "bike", "bus"]

print(vehicles.index("car"))    # 0
print(vehicles.index("bike"))   # 1
print(vehicles.index("bus"))    # 2
