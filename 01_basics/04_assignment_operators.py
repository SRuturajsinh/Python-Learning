"""
Assignment shortcut operators.
These operators update the value of a variable.
"""

score = 100

# Instead of:
score = score + 10
print("Using normal assignment:", score)

score = 100

# Using shortcut assignment
score += 10
print("Using += :", score)

print()

# Other assignment shortcuts
x = 10

x += 5      # x = x + 5
print("After += :", x)

x *= 2      # x = x * 2
print("After *= :", x)

x /= 3      # x = x / 3
print("After /= :", x)

x -= 1      # x = x - 1
print("After -= :", x)

x %= 2      # x = x % 2
print("After %= :", x)

x **= 3     # x = x ** 3
print("After **= :", x)

x //= 2     # x = x // 2
print("After //= :", x)
