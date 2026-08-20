"""
Sorting a list using sort() function.
Sorted but in decreasing order.

Sort this:
list = [1,6,4,2,4,3,5,8,9,7]

"""
# .sort() function can't be assingigned to a variable

list = [1,6,4,2,4,3,5,8,9,7]
print("list:",list) # print the list

list.sort() # Using sort function, it will directly sort the current list
print("sorted list:",list) # print the sorted list 

# sorted() function can be assigned to a variable
l1 = [1,6,4,2,4,3,5,8,9,7]
sorted(l1) # sorted() function sort list and return a new list
a = sorted(l1)
print("l1:",a)

# Reverse sort
l2 = [1,6,4,2,4,3,5,8,9,7]
l2.sort(reverse=False) # reverse=False means it will sort in ascending
print("l2:",l2)
l2.sort(reverse=True) # reverse=True means it will sort in descending
print("l2:",l2)
