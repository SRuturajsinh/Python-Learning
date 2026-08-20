"""
Sorting a List Using sort() and sorted()

This program demonstrates:
1. sort()
2. sorted()
3. Ascending order
4. Descending order
"""

# sort() changes the original list.
# It cannot be assigned to a variable
list = [1,6,4,2,4,3,5,8,9,7]
print("original list:",list) 
list.sort() 
print("sorted list:",list) # print the sorted list 


# sorted() does not change the original list.
# It returns a new sorted list
l1 = [1,6,4,2,4,3,5,8,9,7]
sorted(l1) 
a = sorted(l1)
print("l1:",a)

# Reverse sort
l2 = [1,6,4,2,4,3,5,8,9,7]
l2.sort(reverse=False) # reverse=False means it will sort in ascending
print("l2:",l2)
l2.sort(reverse=True) # reverse=True means it will sort in descending
print("l2:",l2)
