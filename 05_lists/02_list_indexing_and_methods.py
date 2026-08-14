"""
List Indexing and List Methods

This program demonstrates:
1. Accessing list elements
2. Positive and negative indexing
3. Assigning list elements to variables
4. Changing list elements
5. Adding and removing elements
"""


# ============================================================
# 1. ACCESSING ELEMENTS
# ============================================================

fruits = ["apple","banana","cherry","orange","kiwi","melon","mango"]

# Positive indexing starts from 0
#  [   0,        1,        2,        3,       4,       5,       6   ]
#  ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Negative indexing starts from -1
#  [  -7,       -6,       -5,       -4,      -3,      -2,      -1  ]


# Access using positive index
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # cherry

# Access using negative index
print(fruits[-1])  # mango
print(fruits[-2])  # melon
print(fruits[-3])  # kiwi


# ============================================================
# 2. ASSIGNING LIST ELEMENTS TO VARIABLES
# ============================================================

first_fruit = fruits[0]
print(first_fruit)  # apple

second_fruit = fruits[1]
print(second_fruit)  # banana

last_fruit = fruits[-1]
print(last_fruit)  # mango

second_last_fruit = fruits[-2]
print(second_last_fruit)  # melon


# ============================================================
# 3. CHANGING AN ELEMENT
# ============================================================

fruits[0] = "mango"

print(fruits)
# ['mango', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']


# ============================================================
# 4. ADDING ELEMENTS
# ============================================================

# append() adds an item to the end of the list
fruits.append("grape")

print(fruits)
# ['mango', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'grape']


# insert() adds an item at a specific index
fruits.insert(1, "pineapple")

print(fruits)
# 'pineapple' is inserted at index 1


# ============================================================
# 5. REMOVING ELEMENTS
# ============================================================

# remove() removes an item by its value
fruits.remove("banana")

print(fruits)


# del removes an item using its index
del fruits[0]

print(fruits)


# pop() removes an item and returns the removed value
first_fruit = fruits.pop(0)

print("Removed first fruit:", first_fruit)


# pop() without an index removes the last item
last_fruit = fruits.pop()

print("Removed last fruit:", last_fruit)


# Final list
print("Final list:", fruits)
# ['cherry', 'orange', 'kiwi', 'melon', 'mango', 'grape']
