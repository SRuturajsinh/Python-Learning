"""
Loops

Loops repeat a block of code multiple times.

Instead of writing the same code again and again,
you can use loops to automate repetition.
"""
# without loops, we would have to write this code 

print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")

#-------------
# With loops
#-------------

# For loop
for i in range(5):  # range(5) generates numbers: 0, 1, 2, 3, 4
    print("Hello!") # it will print Hello! 5 times

# While loop 
i = 0               # It's Start form here. 
while i < 5:        # Checks condition.
    print("Hello!") # Execution.
    i+=1            # Increments the value of i by 1.

"""
Python does not have a do...while loop like C, C++, or Java.

Why?
In a do...while loop, the code executes at least once, and then the condition is checked.
If the condition is true, the code executes again
But in Python, the code block inside the while loop
"""