"""
Student Scholarship Eligibility System

The program should:

Ask for the student's name.
Ask for age.
Ask for 12th percentage.
Ask if the student belongs to the EWS category (yes/no).

Rules:

Age must be 18 or above.
Percentage must be 75 or above.
EWS must be yes.

If all conditions are met:
Congratulations!
You are eligible for the scholarship.

otherwise:
Sorry!
You are not eligible.
"""


# Here is the Solution.
name=input("Enter your name: ")
age=int(input("Enter your age: "))
if age>=18:
    percentage=float(input("Enter your 12th percentage: "))
    Category=input("Sc/St/OBC/EWS/Genral: ")
else:
    print("Sorry!")
    print("You are not eligible.")
    exit() # exit() will end the program form here.

if  percentage>=75 and Category=="EWS":
    print("Congratulations!")
    print("You are eligible for the scholarship.")
elif  percentage>=60 and (Category=="Sc" or Category=="St"):
     print("Congratulations!")
     print("You are eligible for the scholarship.")

else:
    if percentage>=90 and Category=="Genral":
        print("Congratulations!")
        print("You are eligible for the scholarship.")
    else:
        print("Sorry!")
        print("You are not eligible.")