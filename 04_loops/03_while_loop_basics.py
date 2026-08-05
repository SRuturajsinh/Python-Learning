"""
While Loops in Python
"""

# Increment 
i=1         
while i<10:
    print(i)
    i+=1    # Output : 1,2,3,4,5,6,7,8,9

# Decrement 
i=10
while i>0:
    print(i)
    i-=1    # Output : 10,9,8,7,6,5,4,3,2,1

# Break statement 
i=1
while i<10:
    if i==5:
        break # Stops the loop immediately when the condition is met.
    print(i)
    i+=1    # Output : 1,2,3,4
    
# Continue statement 
i=1
while i<10:
    if i==5:
        continue # Skips the current iteration and continues with the next iteration.
        print(i)
    i+=1    # OutPut : 1,2,3,4,6,7,8,9


"""
This is a basic while loop in python. 
It is used to repeat a block of code until a certain condition is met. 
The condition is evaluated before each iteration of the loop. 
If the condition evaluates to True, the loop is executed again. 
If the condition evaluates to False , the loop terminates."""
