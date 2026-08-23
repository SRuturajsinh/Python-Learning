"""
list comprehension.

You've already covered enough basic list operations. 
This is the next important step before moving on to tuples/sets/dictionaries.
"""

number = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]

# long method using foor loop
sq = []
for i in range(len(number)):
    sq.append(number[i]*number[i])
print("Square number using method1:",sq)

sq1 = []
for number in number:
    sq1.append(number*number)
print("Square number using method2:",sq1)


# list comprehension
square = [number * number for number in number]
print("Square number using list comprehension:",square)


# list comprehension with condition
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nums = [nums for nums in nums if nums%2==0]
print("Even numbers:",even_nums)

"""
Even numbers -> "Even"
Odd numbers  -> "Odd"
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension
result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print("Numbers:", numbers)
print("Result:", result)
