"""
Factorial of a Number

This program calculates the factorial of a user-entered
number using both for and while loops.
"""
num = int(input("Enter a number:"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(str(num)+"! by for loop = ",fact)


num= int(input("Enter a number:"))
fact = 1
i = 1
while i <=num:
    fact = fact * i
    i+=1
print(str(num)+"! by While loop = ",fact)
