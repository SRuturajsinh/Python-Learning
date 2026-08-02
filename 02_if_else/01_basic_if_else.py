"""
This program checks if a person is eligible for a driving license based on their age.
"""
# --- User Input ---
# Get the user's name and store it in the 'name' variable.
name = input("Enter your name: ")
# Ask for the user's age. The input() function returns the age as a string.
age_input = int(input(f"Hello, {name}. Please enter your age: "))
# Convert the age from a string to an integer (a whole number) for comparison.
# if we dont write int than it will cause an error if the user enters text instead of a number.

# --- Eligibility Check ---

# Check if the user's age is greater than or equal to the minimum driving age.
if age_input>= 18: # The 'if' statement evaluates this condition.
    # If the condition is True, than code ends here.
    print(f"Congratulations, {name}! You are eligible for a driving license.")
else:
    # If the condition is False, the 'else' block of code runs instead.
    print(f"Sorry, {name}, you are not yet eligible for a driving license.")
