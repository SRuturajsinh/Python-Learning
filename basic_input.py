"""
This program demonstrates the basic arithmetic operators in Python.
"""
# Addition
print(10+5) # 15

# Subtraction
print(10-5) # 5

# Multiplication
print(10*5) # 50

# Division  
print(10/3) # 3.3333
# Division (/) always returns a float.
print(type(10/3)) # Float

"""
Special operators
"""
# Floor division
print(10//3) # 3
# Floor division (//) returns an integer when both operands are integers.
print(type(10//3)) # Int

# Modulus
print(9%5) # 4
print(10%5) # 0
# This wil give the remainder

# Exponentiation
print(10**2) # 100
# Exponentiation works like Power

"""
Order of operations
Python follows math rules (PEMDAS)
"""
result = 2 + 3 * 4
print("2 + 3 * 4 =", result)

result = (2 + 3) * 4
print("(2 + 3) * 4 =", result)