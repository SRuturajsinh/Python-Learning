"""
Sorting a list without using sort() function.

Sort this:
list = [1,6,4,2,4,3,5,8,9,7]

"""


list = [1,6,4,2,4,3,5,8,9,7]
     # [0,1,2,3,4,5,6,7,8,9]

for i in range(len(list)):
    
    for j in range(i+1):
        if list[i]>list[j]:
            continue
        else:

            # store value before swapping
            a = list[i]
            b = list[j]

            # swap the values
            list[i] = b
            list[j] = a

print("sorted list:",list)
