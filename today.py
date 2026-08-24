"""
Nested Lists

A nested list is a list inside another list.
Here is an example of a nested list:
"""
nested_list = [
    [1,2,3,4],           # We can store numbers
    ["A","B","C"],     # We can store strings
    [True,True,False]  # We can store boolean values
]
# There is 3 list inside one list named nested_list

len(nested_list)

# For accessing the list of the nested list

print(nested_list[0]) # [1,2,3]
print(nested_list[1]) # ["A","B","C"]
print(nested_list[2]) # [True,True,False]

# For accessing the elements of the nested list

print(nested_list[0][0]) # 1
print(nested_list[1][1]) # B
print(nested_list[2][2]) # False

# For accessing the elements of the nested list using a loop

for i in range(0,len(nested_list)): # works for outer list length
    for j in range(0,len(nested_list[i])): # works for inner list length
        print(nested_list[i][j])