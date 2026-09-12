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


# ( * ) lets you collect multiple values

num = [20,30,50,60,43,75] 

*a, b , c =num

print(a) # a = [20,30,50,60]
print(b) # b = [43]
print(c) # c = [75]

"""
This will allow you to assign multiple elements as a list to the single veriable
"""

number = [2,4,3,1,5,6]

*a, rest = number

print(a)   # [2,4,3,1,5]
print(rest)# [6] another remaining elemnts 

# more examples

numbers = [2,4,5,2,1,6,4,6]

a, *b , c = numbers
print(a) # [2]
print(b) # [4,5,2,1,6,4]
print(c) # [6] 

numbers = [2,4,5,2,1,6,4,6]

a,b,*c = numbers
print(a) # [2]
print(b) # [4]
print(c) # [5,2,1,6,4,6]