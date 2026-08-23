"""
Even numbers -> "Even"
Odd numbers  -> "Odd"
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension
result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print("Numbers:", numbers)
print("Result:", result)
