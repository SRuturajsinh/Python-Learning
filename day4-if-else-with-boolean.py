"""this is log in program made using boolean and if else statement"""

print("-------Log In-------")

user_name = input("Enter your Username: ")
correct_username = user_name == "Ruturaj1310" # == is boolean oparator 

if correct_username: # if it is True than this condition will be run
    print("Correct Username")
    print("Welcome back", user_name)

    password = int(input("Enter Password: "))
    correct_password = password == 101010

    if correct_password: # if True
        print("Successfully logged in")
    else: # False
        print("Incorrect Password")
else: # False
    print("Invalid Username")
