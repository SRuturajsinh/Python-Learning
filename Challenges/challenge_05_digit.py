"""
Count the number of digits in a number
using function, while loop and for loop.
"""

# Using Function
num=int(input("Enter a Number: "))
length=len(str(num))
print(f"Number of digits by function: {length}")

# Using while loop
count=0
while num>0:
    # code will run until the num = num//10 = 0
    num=num//10
    count=count+1
print(f"Number of digits by while loop: {count}")

# Using for loop
num=int(input("Enter a Number: "))
count=0
for i in range(num,0,-1):
    num=num//10
   # Suppose num = 123:
    # 123 // 10 = 12, which is not equal to 0.
    # So count = 0 + 1 = 1.
    #
    # Now num = 12:
    # 12 // 10 = 1, which is not equal to 0.
    # So count = 1 + 1 = 2.
    #
    # Finally num = 1:
    # 1 // 10 = 0, which is equal to 0.
    # So count = 2 + 1 = 3.
    #
    # break stops the loop and count remains 3.

    if num==0:
        count=count+1
        break
    else:
        count=count+1
print(f"Number of digits by for loop: {count}")
