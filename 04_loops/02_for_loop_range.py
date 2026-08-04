"""
For Loops in Python

This program demonstrates how to use the range() function
with different arguments in a for loop.
"""

# (stop)
for i in range (10):
    print(i)       # It will print numbers from 0 to 9


 # (start,stop)
for i in range (1,10):
    print(i)       # It will print numbers from 1 to 9


# (start,stop,step)
for i in range (1,10,2):
    print(i)       # It will print numbers from 1 to 9 with a diffrance of 2
                   # OutPut: 1 , 3 ,5 ,7 ,9


# (start,stop,step)
for i in range (10,1,-2):
    print(i)       # It will print numbers from 10 to 1 with a difference of -2
                   # OutPut: 10 , 8 , 6 , 4 , 2

"""
range function is used to generate a sequence of numbers.
It takes three arguments in the form of range(start, stop, step)

start : Starting value of the sequence.
stop  : Ending value (not included).
step  : Number added or subtracted in each iteration.
"""
