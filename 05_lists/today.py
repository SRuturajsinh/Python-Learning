"""
list slicing

[start:stop]
[:stop]
[start:]
[start:stop:step]
"""
list = ["apple","kiwi","mango","banana","cherry","orange"]
    #  [   0   ,   1  ,   2   ,   3    ,   4    ,   5    ]
    #  [  -6   ,  -5  ,  -4   ,  -3    ,  -2    ,  -1    ]
#==============================
# [start:stop]
#==============================

print(list[1:4])
# ["kiwi", "mango", "banana"]

print(list[0:len(list)])
# ["apple", "kiwi", "mango", "banana", "cherry", "orange"]

#==============================
# [:stop]
#==============================

print(list[:3])
# ["apple", "kiwi", "mango"]

print(list[:-1])
# ["apple", "kiwi", "mango", "banana", "cherry"]

#==============================
# [start:]
#==============================

print(list[2:])
# ["mango", "banana", "cherry", "orange"]

print(list[-3:])
# ["banana", "cherry","orange"]

#==============================
# [start:stop:step]
#==============================

print(list[1:5:2])
# ["kiwi", "banana"]

print(list[0:len(list):3])
# ["apple", "banana"]
