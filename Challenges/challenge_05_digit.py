"""
Count the number of digits in a number
using function, while loop and for loop.
"""

# Using Function
num=int(input("Enter a Number: "))
lenght=len(str(num))
print(f"Number of digits by function: {lenght}")

# Using while loop
count=0
while num>0:
    num=num//10
    count=count+1
print(f"Number of digits by while loop: {count}")
