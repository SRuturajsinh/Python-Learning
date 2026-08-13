"""
Reverse a Entered number

Example:
Input: 12345
Output: 54321
"""

# Via while loop reverse number program
num = int(input("Enter a number: "))
rev_num = 0
while num>0:
    rem = num%10
    rev_num = rev_num*10 + rem
    num = num//10
    
print(f"Reversed number: {rev_num}")

# Via for loop reverse number program
rev_num = 0
num = int(input("Enter a number: "))
for i in range(num):
    if num == 0:
        break
    else:
     reminder = num % 10
     rev_num = rev_num * 10 + reminder
     num = num // 10

print(f"Reversed number: {rev_num}")