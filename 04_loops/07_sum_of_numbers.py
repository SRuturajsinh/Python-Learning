"""
Sum of Numbers Using For and While Loops

This program calculates the sum of numbers from
1 to a user-given number using both for and while loops.
"""

num=int(input("Enter a number:"))
total=0
# for loop
for i in range(num,0,-1):
    total=total+i
print("Output by for loop:",total)


num=int(input("Enter a number:"))
# while loop
total=0
i=num

while i>0:
    total=total+i
    i-=1
print("Output by while loop:",total)
