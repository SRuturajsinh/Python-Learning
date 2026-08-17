"""
List Methods

In this program we will learn:

append()  - add to the end
insert()  - add at a specific position
extend()  - add multiple elements
remove()  - remove by value
pop()     - remove by index and return the item
del       - delete by index
clear()   - remove everything
"""


# ==================================================
# append()
# Add an item to the end of the list
# ==================================================

numbers = []

numbers.append(1)
numbers.append(2)
numbers.append(3)

print("numbers:", numbers)


# ==================================================
# insert()
# Add an item at a specific position
# ==================================================

fruits = ["apple", "banana", "cherry"]

fruits.insert(1, "orange")
print(fruits)

fruits.insert(len(fruits), "pear")
print(fruits)

fruits.insert(len(fruits) - 1, "mango")
print("fruits:", fruits)


# ==================================================
# extend()
# Add multiple elements to a list
# ==================================================

elements = ["car", "bike", "train", "bus"]

elements.extend(["cycle", "boat", "ship"])

print("elements:", elements)


# ==================================================
# remove()
# Remove an item by its value
# ==================================================

numbers = [1, 2, 3]

numbers.remove(2)

print("numbers:", numbers)


letters = ["a", "b", "c", "d"]

letters.remove("b")

print("letters:", letters)


# ==================================================
# pop()
# Remove an item by index
# pop() also returns the removed item
# ==================================================

numbers = [1, 2, 3, 4, 5]

removed_number = numbers.pop(2)

print("Removed:", removed_number)
print("numbers:", numbers)


letters = ["a", "b", "c", "d"]

removed_letter = letters.pop(1)

print("Removed:", removed_letter)
print("letters:", letters)


# ==================================================
# del
# Delete an item by index
# ==================================================

numbers = [1, 2, 3, 4, 5]

del numbers[2]

print("numbers:", numbers)


letters = ["a", "b", "c", "d"]

del letters[1]

print("letters:", letters)


# ==================================================
# clear()
# Remove all elements from the list
# ==================================================

numbers = [1, 2, 3, 4, 5]

numbers.clear()

print("numbers:", numbers)