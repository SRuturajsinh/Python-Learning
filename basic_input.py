"""This is a simple program that takes user input for their name, age,
 favorite programming language, and city. 
 It then performs some basic operations and prints the results."""


name=input("Enter your name: ")
age=int(input("Enter your age: "))
fav_programing_lan=input("Enter your favorite programming language: ")
city=input("Enter your city: ")

print(len(name))

if (age)>18:
    print("Excellent!")
else:
    print("You are young but also eligible for this program.")

print(type(age))

print(name*3)

print("\n----- User Information -----")
print("Name:", name)
print("Age:", age)
print("Favorite Language:", fav_programing_lan)
print("City:", city)