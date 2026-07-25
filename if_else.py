"""this is simple program for if else statement"""
"""USER WILL ENTER HIS AGE AND PROGRAM WILL CHECK IF HE IS ELIGIBLE TO VOTE OR NOT"""

name=input("Enter your name: ")
age=int(input("Enter your age: "))

print("Hello",name)
if age>=18:
    print("you are eligible for APPLICATION")

    print("---------APPlICATION FORM---------")
    maths=int(input("Enter your marks in Maths: "))
    science=int(input("Enter your marks in Science: "))
    english=int(input("Enter your marks in English: "))

    if maths>100 or science>100 or english>100:
        print("Please enter valid marks")
    else:
        total=maths+science+english
        print("Total marks:",total)
        percentage=(total/300)*100
        print("Percentage:",percentage)

        if percentage>=90:
            print("congratulations! ",name," you are selected for this vacancy")
        elif percentage>=80:
            print("you have scored ",percentage," % wait for next round")
        else:
            print("sorry! ",name," you are not selected for this vacancy")
else:
    print("you are not eligible for APPLICATION")

