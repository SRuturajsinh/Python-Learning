"""
Sum of even numbers from 1 to n
using for loop and while loop.
"""
# For input integer
num = int(input("Enter a Even Number: "))

# Via for loop
total=0
for i in range(2,num+1,2):
    # Start from 2 and increase by 2.
    # This gives only even numbers:
    # 2, 4, 6, 8, ...
    total= i+total
print(total)

# Via while loop
i=2
total=0
while(i<=num):
     # Continue until i becomes greater than num.
    total=i+total
    i=i+2
print(total)