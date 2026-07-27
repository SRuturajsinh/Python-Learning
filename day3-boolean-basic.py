"""
This program demonstrates Boolean values in Python.
It checks whether a person's age makes them eligible to vote.
"""

# Direct assingment
is_eligible=True # or else we can take false

age=20 # data entered 
can_vote=age>=18 # check if the person is eligible to vote
print("Age:", age, "- Can vote:", can_vote) # print the result by can_vote variable which is a boolean value.



person1_age = 10
can_vote = person1_age >= 18
print("Age:", person1_age, "- Can vote:", can_vote)

person2_age = 18
can_vote = person2_age >= 18
print("Age:", person2_age, "- Can vote:", can_vote)

"""
Comparison operators such as >=, <=, ==, and !=
return Boolean values (True or False).

Example:
age >= 18

If the expression is True, the result is True.
Otherwise, it is False.
"""

print(10>=5) # Ture
print(30!=10) # True
print(10<=5) # False
print(10==10) # True
